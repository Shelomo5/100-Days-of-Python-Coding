from flask import Flask, render_template, request
import requests
import smtplib
import os


posts = requests.get("https://api.npoint.io/3e2686b00fc18d39a275").json()

# gmail password and email
my_email = os.environ["my_email"]
password = os.environ["password"]

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


# Route to receive data from the form
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    # if form data is submitted then sent message displayed as opposed to contact me default
    if request.method == "POST":
        data = request.form
        email_send(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", message="Successfully sent your message")
    return render_template("contact.html", message="Contact Me")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


# Sending email when form submitted on blog
def email_send(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(my_email, my_email, email_message)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
