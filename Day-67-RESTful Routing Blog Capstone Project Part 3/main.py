from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)

# instantiating CKEditor
ckeditor = CKEditor(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()

# Form to add a blog post
class CreatePostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    img_url = StringField('Image_url', validators=[DataRequired(), URL()])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit Post')


@app.route('/')
def get_all_posts():
    # query created to select all posts from database
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)

# Route allows user to click on individual posts
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Pulling a specific blog post database using post_id
    requested_post = db.session.query(BlogPost).get(post_id)
    return render_template("post.html", post=requested_post)


# Route allows user to create new post
@app.route("/new-post", methods=['GET', 'POST'])
def add_new_post():
    # Instantiating form
    form = CreatePostForm()
    # Date
    post_date = date.today().strftime('%B %d, %Y')
    # Will check if it is a POST request and if it is valid
    if form.validate_on_submit():
        new_post = BlogPost(
                            title=request.form.get("title"),
                            body=request.form.get("body"),
                            img_url=request.form.get("image_url"),
                            author=request.form.get("author"),
                            subtitle=request.form.get("subtitle"),
                            date=post_date,
                            )
        db.session.add(new_post)
        db.session.commit()

        # Rendering form on html
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)

# route to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    # Pulling the post to edit in our database using its id
    blog_post = db.session.query(BlogPost).get(post_id)
    # Instantiating form
    edit_form = CreatePostForm(
            title=blog_post.title,
            subtitle=blog_post.subtitle,
            img_url=blog_post.img_url,
            author=blog_post.author,
            body=blog_post.body
    )
    # Updating database with form data after user edits form
    if edit_form.validate_on_submit():
        blog_post.title = edit_form.title.data
        blog_post.subtitle = edit_form.subtitle.data
        blog_post.img_url = edit_form.img_url.data
        blog_post.author = edit_form.author.data
        blog_post.body = edit_form.body.data

        db.session.commit()

        # Redirect user to show_post route along with the id
        return redirect(url_for("show_post", post_id=blog_post.id))
    # Passing form to make-post.html
    return render_template("make-post.html", form = edit_form)

# Route deletes a blog post from the database
@app.route("/delete/<int:post_id>", methods=["DELETE", "POST", "GET"])
def delete_post(post_id):
    # We are pulling the post to delete in our database by its id
    post_delete = db.session.query(BlogPost).get(post_id)
    db.session.delete(post_delete)
    db.session.commit()
    # Redirect to homepage
    return redirect(url_for("get_all_posts"))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
