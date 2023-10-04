from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# instantiating login_manager class
login_manager = LoginManager()
# Configure object for login
login_manager.init_app(app)

# Reloads user object using user_id stored in the session
@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

# CREATE TABLE IN DB
# Mixin provides multiple inheritance to Python
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")

# Route registers users
@app.route('/register', methods=['GET','POST'])
def register():
    # If user clicks on "sign me up" button
    if request.method == "POST":
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
            password = hashed_password
        )
        # Adding a user object in the database
        db.session.add(add_user)
        db.session.commit()

        # Name parameter passed to url for secrets route
        return redirect(url_for('secrets', name = add_user.name))
    # Send user to register.html to register
    return render_template("register.html")

# Route allows players to login
@app.route('/login', methods=['GET','POST'])
def login():
    # If user clicks on "Login" button
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        # finding the user based on email entered
        finding_user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if finding_user:
            # If the hashed password and entered password are the same
            if check_password_hash(pwhash=finding_user.password, password=password):
                # Function authenticates user for login
                login_user(finding_user)
                # redirect to secrets the html
                return redirect(url_for("secrets"))
            else:
                flash("Password was incorrect please try again.")
                return redirect(url_for('login'))
        else:
            flash("Email wasn't found please try again.")
            return redirect(url_for('login'))

    return render_template("login.html")

# Route allows user to download file after registering
@app.route('/secrets')
@login_required
def secrets():
    # Grab hold of name parameter in url
    name = request.args.get('name')
    # Name parameter passed to secrets.html
    return render_template("secrets.html",name=name)

# Route logs out user
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

#  Route allows user to download cheat sheet
@app.route('/download')
@login_required
def download():
    # download the cheat_sheet.pdf file when user clicks download button
    #  offers to save the file as_attachment
    return send_from_directory(directory="static", path="files/cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
