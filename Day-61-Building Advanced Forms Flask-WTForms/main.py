from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5


# class defines the fields the form will have
# defining class variables are instantiations of the fields
# label is the human-readable name for each field
class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")

app = Flask(__name__)
app.secret_key = "string_secret"
# initialise bootstrap flask
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')

# login route which renders login.html
@app.route('/login', methods=['GET', 'POST'])
def login():
    # instance created
    form = MyForm()
    # check if user submitted the form (checking POST request)
    if form.validate_on_submit():
       # if the email and password entered are correct return success page
       if form.email.data == "admin@email.com" and form.password.data == "12345678":
           return render_template("success.html")
       else:
           return render_template("denied.html")
    # renders login.html which contains form
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
