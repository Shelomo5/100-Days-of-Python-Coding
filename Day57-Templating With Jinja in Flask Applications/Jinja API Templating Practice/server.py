from flask import Flask, render_template
import random
import datetime
import requests

# creating app object from Flask class
app = Flask(__name__)

# decorator for homepage route
@app.route('/')
def home(name=None):
    # Generates random integer
    random_number = random.randint(1, 10)

    # Using datetime to get the year
    current_year = datetime.datetime.now().year

    # Renders html template that's inside templates file
    return render_template('index.html', num=random_number, year=current_year)

# parsing url to take some_name, entered by user, as an argument
@app.route('/guess/<some_name>')
# name_guess function goes through decorator method above and gets value for some_name variable
def name_guess(some_name):
    genderize_r = requests.get(f"https://api.genderize.io?name={some_name}")
    current_gender = genderize_r.json()['gender']
    agify_r = requests.get(f"https://api.agify.io?name={some_name}")
    current_age = agify_r.json()['age']

    # values obtained from name, gender, and age are passed into html template
    return render_template('guess.html', name=some_name, gen=current_gender, age=current_age)

@app.route("/blog/<num>")
# function fetches all blogs from url/api
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_data = response.json()
    # all_data passed into blog.html
    return render_template('blog.html', posts=all_data)

# initiates flask
if __name__ == "__main__":
    app.run(debug=True)