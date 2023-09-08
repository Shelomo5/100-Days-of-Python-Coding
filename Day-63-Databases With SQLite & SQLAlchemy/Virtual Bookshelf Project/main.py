from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()

# Create The App
app = Flask(__name__)

# Creating New SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books.db"

# Initialize the app with the extension
db.init_app(app)

# Create New Table
class Book(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   title = db.Column(db.String(250), unique=True, nullable=False )
   author = db.Column(db.String(250), nullable=False)
   rating = db.Column(db.Float, nullable=False)

# Creating the table schema in the database
with app.app_context():
   db.create_all()


@app.route('/')
def home():
    # Create a "query" to select from the database
    # result = the rows in the database
    result = db.session.execute(db.select(Book).order_by(Book.title))
    # scalars() used to get the individual elements rather than entire rows
    all_books = result.scalars()
    # all books is passed to rendered in index.html
    return render_template("index.html", books=all_books)

# add new books via the /add route
@app.route("/add", methods=["GET", "POST"])
def add():
    # check if user submitted the form (checking POST request)
    if request.method == "POST":
        # instantiate book class to create book object
        add_book = Book(
            title = request.form["book_name"],
            author = request.form["book_author"],
            rating = request.form["book_rating"]
        )
        # Creating a new book record in the database by adding book object
        db.session.add(add_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route('/edit_rating', methods=["GET", "POST"])
# Updating the record
def edit_rating():
    # If user clicks on Change Rating button hence updating database
    if request.method == "POST":
        # We get book ID from the form we just submitted/posted
        book_id = request.form["id"]
        # Book_id used to select book to edit from database:
        book_to_update = Book.query.get(book_id)
        # New rating that the user typed in the form
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    # When clicking on Edit Rating link "GET" is used not "POST" and url is generated
    # This line gets id parameter from the URL generated anchor link in index.html
    # Id passed to edit_rating route as a query parameter in the html: http://localhost:5000/edit_rating?id=1
    book_id = request.args.get('id')
    # book_id is used to select the book to edit from database
    book_selected = Book.query.get(book_id)
    # pass entire book to edit page
    return render_template("edit.html", book=book_selected)

@app.route('/delete', methods=["GET", "POST"])
# Updating the record
def delete():
    # gets id which was passed in generated url
    book_id = request.args.get('id')
    # id used to find book in database
    book_to_delete = db.get_or_404(Book, book_id)
    # book deleted
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

