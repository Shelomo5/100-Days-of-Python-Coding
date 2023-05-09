from flask import Flask
import random

# creating app object from Flask class
app = Flask(__name__)

# Generating random number
random_num = random.randint(0, 9)
print(random_num)

# Python decorator for homepage route
@app.route('/')
def homepage_route():
    # Text and image
    return '<h1> Guess a number between 0 and 9 </h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'

# integer converter added to url and function receives integer as an argument
@app.route('/<int:guess>')
# Depending on if number guessed correctly or guess is too low or high, user is directed to different path
def guess_number(guess):
    if guess == random_num:
        return "<h1 style='color: green'> You found me</h1>" \
               "<img src='https://media.giphy.com/media/dudcZA9e14HIY/giphy.gif' width=600>"
    elif guess < random_num:
        return f"<h1 style='color: orange'> {guess} is too Low</h1>"\
               "<img src='https://media.giphy.com/media/yT7JPIdGb5oJO/giphy.gif' width=600>"
    elif guess > random_num:
        return f"<h1 style='color: red'> {guess} is too High</h1>"\
               "<img src='https://media.giphy.com/media/1gPAjJNxzwV99v05Ze/giphy.gif' width=600>"


# runs flask
app.run(debug=True)