from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
import requests
from wtforms import form, StringField, SubmitField, FloatField

MOVIE_API_KEY = "c97549e0b31ecdd9d08c25f29c2237c7"
MOVIE_DB_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Creating New SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
# create the extension
db = SQLAlchemy()
# Initialize the app with the extension
db.init_app(app)

# Create New Movie Table
class Movie(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   title = db.Column(db.String(250), unique=True, nullable=False )
   year = db.Column(db.Integer, nullable=False)
   description = db.Column(db.String(500), nullable=False)
   rating = db.Column(db.Float, nullable=True)
   ranking = db.Column(db.Integer, nullable=True)
   review = db.Column(db.String(250), nullable=True)
   img_url = db.Column(db.String(250), nullable=False)

# Creating the table schema in the database
with app.app_context():
   db.create_all()

# Form created to edit rating and review of a movie
class MovieForm(FlaskForm):
   rating = FloatField("Your Rating Out of 10 e.g. 7.5")
   review = StringField("Your Review")
   submit = SubmitField("Done")

# Form to add movie
class AddMovieForm(FlaskForm):
   title = StringField("Movie Title", validators=[DataRequired()])
   submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
   # query created to select all movies from database into a list
   # .all() generates a list from query result
   all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()
   i = 1
   # Using for loop to assign a ranking to each movie
   for movie in all_movies:
      movie.ranking = i
      i += 1
   db.session.commit()
   return render_template("index.html", movies=all_movies)


@app.route("/change_rating", methods=['GET','POST'])
def change_rating():
   form = MovieForm()
   # Extracts query parameter (the movie id) from url
   movie_id = request.args.get('id')
   # Movie_id is used to select the book to edit from database
   movie_updated = Movie.query.get(movie_id)
   # will check if it is a POST(form submitted) request and if it is valid
   if form.validate_on_submit():
      movie_updated.rating = form.rating.data
      movie_updated.review = f'"{form.review.data}"'
      db.session.commit()
      # return to homepage after updating ratings and reviews
      return redirect(url_for('home'))
   return render_template('edit.html', movie=movie_updated, form=form)

@app.route("/delete", methods=['GET','POST'])
def delete():
   # gets id which was passed in generated url
   movie_id = request.args.get('id')
   # id used to find movie in database
   movie_to_delete = db.get_or_404(Movie, movie_id)
   # movie deleted
   db.session.delete(movie_to_delete)
   db.session.commit()
   return redirect(url_for('home'))


# Add movie route
@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
   # instantiating form
   form = AddMovieForm()
   if form.validate_on_submit():
      # movie entered by user in form
      movie_entered = form.title.data
      # making request to api
      response = requests.get(url=MOVIE_DB_URL,params={'api_key': MOVIE_API_KEY, 'query': movie_entered})
      response.raise_for_status()
      data = response.json()["results"]
      print(data)
      #rendering select.html page and passing data there
      return render_template("select.html", options=data)
   # Passing form while generating add html
   return render_template('add.html', form=form)

# Get movie details
@app.route("/get_details", methods=["GET", "POST"])
def get_details():
   # gets id from movie database of movie clicked by user which was passed in generated url in select.html
   movie_id = request.args.get('id')
   if movie_id:
      movie_url = f"{MOVIE_DB_INFO_URL}/{movie_id}"
      response = requests.get(movie_url, params={'api_key': MOVIE_API_KEY, "language": "en-US"})
      data = response.json()
      print(data)
      add_movie = Movie(
         title=data["title"],
         img_url=f"{MOVIE_DB_IMAGE_URL}/{data['poster_path']}",
         year=data["release_date"].split("-")[0],
         description=data["overview"]
      )
      # Creating a new movie record in the database by adding movie object
      db.session.add(add_movie)
      db.session.commit()
      # Redirect to change_rating to update the movie entry with rating and review
      return redirect(url_for('change_rating', id=add_movie.id))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
