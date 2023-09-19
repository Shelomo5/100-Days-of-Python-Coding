from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
# db is the sql-database function/object
db = SQLAlchemy()
db.init_app(app)

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    # Method uses dict comprehension to convert data to key value pairs
    # Iterating through each data column and pairing column name (key) with value of the column
    def to_dict(self):
        final_dict = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return final_dict

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

# Randomly selects a cafe from database
@app.route("/random")
def random_choice():
    # query created to select all cafes from database into a list
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    # randomly selecting a cafe
    random_choice = random.choice(all_cafes)
    # converting random_choice to dictionary using .to_dict() and then using jsonify() to convert it to JSON.
    json_cafe = jsonify(cafe = random_choice.to_dict())
    return json_cafe

# Get all cafes from database
@app.route("/all", methods=['GET','POST'])
def get_all():
    # query created to select all cafes from database into a list
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name.desc())).scalars().all()
    return jsonify(cafes = [cafe.to_dict() for cafe in all_cafes])

# Find cafe by location
@app.route("/search", methods=['GET','POST'])
def location_find_cafe():
    # gets location of cafe as a parameter in url
    cafe_location = request.args.get('loc').title()
    # filters database base on cafe_location
    cafe_result = db.session.execute(db.select(Cafe).where(Cafe.location == cafe_location)).scalars().all()
    if cafe_result:
        # return found cafe in JSON format
        return jsonify(cafe=[cafe.to_dict() for cafe in cafe_result])
    else:
        return jsonify(error={'Not Found': "Sorry, we don't have a cafe at that location"})

# Add a Cafe to the database
@app.route("/add", methods=['POST'])
def new_cafe():
    # Instantiating cafe class
    add_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        seats = request.form.get("seats"),
        has_toilet = int(request.form.get("has_toilet")),
        has_wifi = int(request.form.get("has_wifi")),
        has_sockets = int(request.form.get("has_sockets")),
        can_take_calls = int(request.form.get("can_take_calls")),
        coffee_price = request.form.get("coffee_price")
    )
    # Creating a new cafe record in the database
    db.session.add(add_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# Route to update coffee price
@app.route("/update-price/<int:cafe_id>", methods=['PATCH','GET','POST'])
def price_update(cafe_id):
    # gets the new price of cafe as a parameter in url
    new_price = request.args.get("new_price")
    # We are pulling the cafe to update in our database with id
    cafe_udpate = db.session.query(Cafe).get(cafe_id)
    # if cafe is found
    if cafe_udpate:
        # Price updated
        cafe_udpate.coffee_price = new_price
        db.session.commit()
        # return 200 message to show it was successful
        return jsonify(response={'success': 'Successfully update the cafe coffee price'}), 200
    else:
        # return 404 message to show it was unsuccessful
        return jsonify(response={'not found': 'The cafe coffee price was unable to be updated'}), 404

# Route to delete a cafe if it closes
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE", "POST", "GET"])
def delete_cafe(cafe_id):
    # We are pulling the cafe to delete in our database with its id
    cafe_delete = db.session.query(Cafe).get(cafe_id)
    # Gets the api_key as a parameter in url
    api_key = request.args.get("api-key")
    # if the API key passed in URL is correct
    if api_key == "TopSecretAPIKey":
        # If cafe to delete is found
        if cafe_delete:
            # cafe deleted
            db.session.delete(cafe_delete)
            db.session.commit()
            # return 200 message to show it was successful
            return jsonify(response={'success': 'Successfully deleted the cafe'}), 200
        else:
            # return 404 message to show it was unsuccessful
            return jsonify(response={'not found': 'The cafe was not found and could not be deleted'}), 404
    else:
        # return 403 message to show access is not granted
        return jsonify(response={'error': 'Make sure you have put in the correct api_key'}), 403

    

if __name__ == '__main__':
    app.run(debug=True)
