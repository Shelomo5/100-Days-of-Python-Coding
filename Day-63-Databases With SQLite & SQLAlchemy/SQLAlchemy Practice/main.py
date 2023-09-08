from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# create the extension
db = SQLAlchemy()

# Create The App
app = Flask(__name__)

# # Creating New SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Initialize the app with the extension
db.init_app(app)

# Create New Table
class Book(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   title = db.Column(db.String(250), unique=True, nullable=False )
   author = db.Column(db.String(250), nullable=False)
   rating = db.Column(db.Float, nullable=False)

   # This allows each book object to be identified by its title when printed.
   def __repr__(self):
       return f'<Book {self.title}>'

# Creating the table schema in the database
with app.app_context():
   db.create_all()

# Creating a New Record
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    new_book_2 = Book(id=2, title="Harry Potter2", author="JK Rowling", rating=9.4)
    new_book_3 = Book(id=3, title="Harry Potter3", author="JK Rowling", rating=9.5)
    db.session.add(new_book_3)
    db.session.commit()

# Read All Records
with app.app_context():
    # Create a "query" to select from the database
    # result represents the rows in the database
    result = db.session.execute(db.select(Book).order_by(Book.title))
    # scalars() used to get the individual elements rather than entire rows
    all_books = result.scalars()

# To get a single element we can use scalar() instead of scalars()
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

# Update A Particular Record By Query
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

# Update A Record By PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

# Delete A Particular Record By PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()