from flask import Flask, render_template
import requests
from post import Post


# creating app object from Flask class
app = Flask(__name__)

# API request to get blog data
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_entries = response.json()

# Empty list to store data
entries_list = []

# iterating through all_entries json response
for entry in all_entries:
    # for each blog entry creating an instance of the Post class with 4 attributes which contain blog data from API
   object = Post(entry["id"], entry["title"], entry["subtitle"], entry["body"])
    # append each object to list
   entries_list.append(object)

# Home route
@app.route("/")
# render list containing Post class objects containing API data to index.html
def get_blog():
    return render_template('index.html', posts=entries_list)

# adding to url post_num, the id number associated to each hyperlink in home route
@app.route("/post/<int:post_num>")
# function receives post_num as keyword argument
def display_post(post_num):
    # the blog post requested by user variable
   requested_post = None
    # iterating through list containg blog data
   for blog_post in entries_list:
       # if the id in blog data list matches the id of the hyperlink clicked by user
      if blog_post.id == post_num:
          # blog requested by user is the same as the given object in entries_list
         requested_post = blog_post
    # render post.html file template and pass requested_post value as key word argument
   return render_template('post.html', entry=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
