from flask import Flask, render_template, request

# creating app object from Flask class
app = Flask(__name__)


# decorator for homepage route
@app.route('/')
def home():
    # render index.html page
    return render_template('index.html')

# Using HTTP methods POST to send form data to Flask server
# GET is not secured POST is usually form data
# decorator will trigger a method when it receives a POST request
@app.route('/login', methods=['POST'])
def receive_data():
    # request.form gives us form data entered by user as a dictionary
    # the name attribute in input is the key
    name = request.form["username"]
    password = request.form['password']
    return f"<h1>Name: {name}, Password: {password}</h1>"







    # initiates flask
if __name__ == "__main__":
    app.run(debug=True)