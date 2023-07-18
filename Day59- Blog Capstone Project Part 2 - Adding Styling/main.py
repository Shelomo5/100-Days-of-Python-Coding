from flask import Flask, render_template
import requests

# creating app object from Flask class
app = Flask(__name__)

# request made to n:point api which contains blog data
api_endpoint = "https://api.npoint.io/3e2686b00fc18d39a275"
response = requests.get(api_endpoint)
entries = response.json()


# decorator for homepage route
@app.route('/')
def home():
    # render index.html file template and pass api blog data as a key word argument
    return render_template('index.html', all_entries=entries)


# render about.html file template
@app.route('/about')
def about():
    return render_template('about.html')


# render contact.html file template
@app.route('/contact')
def contact():
    return render_template('contact.html')


# adding to url entry_num, the id number associated to each entry in home route
@app.route("/entry/<int:entry_num>")
# function receives entry_num as keyword argument
def show_entry(entry_num):
    # variable for the blog post requested by user
    requested_post = None
    # iterating through blog data
    for blog_post in entries:
        # if the id in blog data list matches the id of the hyperlink clicked by user
        if blog_post["id"] == entry_num:
            # then they are the same
            requested_post = blog_post
    # render post.html file template and pass requested_post value as key word argument
    return render_template('post.html', entry=requested_post)


# initiates flask
if __name__ == "__main__":
    app.run(debug=True)
