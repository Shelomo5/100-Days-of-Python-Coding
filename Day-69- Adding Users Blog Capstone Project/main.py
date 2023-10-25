from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# instantiating login_manager class
login_manager = LoginManager()
# Configure object for login
login_manager.init_app(app)

# Initialize gravatar with flask application
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# Reloads user object using user_id stored in the session
@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

# Decorator function for admin_only access
def admin_only(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # If user is logged in and his id is 1
        if current_user.is_authenticated and current_user.id == 1:
            # Continue with the route function
            return f(*args, **kwargs)
        else:
            # return abort with 403 error
            return abort(403)
    return wrapper

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# User table for all your registered users.
# Mixin provides multiple inheritance to Python
class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    # Creating One to Many relationship because one user can have many blogposts
    # Creating posts column in User Table
    # "author" refers to column in BlogPost table (child) as to connect a blog post to its author (parent User table)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")

# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # Creating "author" column in BlogPost table
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="parent_post")

# Table allows user to write comments to blog posts
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    # Creating relationship with comments attribute of User table
    comment_author = relationship("User", back_populates="comments")
    # foreign key serves to reference the primary key of another existing table
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")



with app.app_context():
    db.create_all()


# Using Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=["GET", "POST"])
def register():
    # Instantiating form
    register_form = RegisterForm()
    # If user clicks on "sign me up" button
    if register_form.validate_on_submit():
        # Getting email input in form
        email = request.form.get('email')
        # Checking if email is already in register
        already_exists = db.session.query(User).where(User.email == email).scalar()
        # If an email was found in database
        if already_exists:
            flash("Email is already registered please use same email to login.")
            return redirect(url_for('login'))

        # number of characters in the salt
        salt_length = 8
        #  hash method and iterations(rounds of salting)
        hash_method = 'pbkdf2:sha256:100000'
        password = request.form.get("password")

        hashed_password = generate_password_hash(password, method=hash_method, salt_length=salt_length)

        # Instantiating user class
        add_user = User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            password=hashed_password
        )
        # Adding a user object in the database
        db.session.add(add_user)
        db.session.commit()

        # Authenticates user for login
        login_user(add_user)
        # Redirect to get_all_posts after use has been added
        return redirect(url_for('get_all_posts'))
    # Send user to register.html to register and pass the form
    return render_template("register.html", form=register_form, current_user=current_user)

# Retrieve a user from the database based on their email.
@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    # If user clicks on "Login" button
    if login_form.validate_on_submit():
        email = request.form.get("email")
        password = request.form.get("password")
        # finding the user based on email entered
        finding_user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if finding_user:
            # If the hashed password and entered password are the same
            if check_password_hash(pwhash=finding_user.password, password=password):
                # Function authenticates user for login
                login_user(finding_user)
                # redirect to homepage after user logs in
                return redirect(url_for("get_all_posts"))
            else:
                flash("Password was incorrect please try again.")
                return redirect(url_for('login'))
        else:
            flash("Email wasn't found please try again.")
            return redirect(url_for('login'))
    return render_template("login.html", form= login_form, current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, current_user=current_user)


# Show post and allow logged-in users to comment on post
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    # Find post in database by id
    requested_post = db.get_or_404(BlogPost, post_id)
    # Instantiate form class
    form = CommentForm()

    # Will check if it is a POST request and if it is valid
    if form.validate_on_submit():
        # If user is not logged in
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))
        # Create new comment
        new_comment = Comment(
            text=form.commment_input.data,
            comment_author=current_user,
            parent_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
        # Clear the comment box after submission
        form.commment_input.data = ""

    return render_template("post.html", post=requested_post, current_user=current_user, form=form, gravatar=gravatar)


@app.route("/new-post", methods=["GET", "POST"])
# Using a decorator so only an admin user can create a new post
@admin_only
def add_new_post():
    # Instantiate form class
    form = CreatePostForm()
    # Will check if it is a POST request and if it is valid
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, current_user=current_user)



@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
# Using a decorator so only an admin user can edit a post
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)


@app.route("/delete/<int:post_id>")
# Using a decorator so only an admin user can delete a post
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@app.route("/contact")
def contact():
    return render_template("contact.html", current_user=current_user)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
