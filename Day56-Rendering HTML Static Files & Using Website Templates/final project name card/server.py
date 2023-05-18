from flask import Flask, render_template

# creating app object from Flask class
app = Flask(__name__)

# decorator for homepage route
@app.route('/')
def homepage(name=None):
    # Renders html template
    return render_template('index.html', name=name)

# initiates flask
if __name__ == "__main__":
    app.run(debug=True)