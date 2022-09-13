from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice


app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
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


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

# GET random cafe
@app.route("/random")
def get_random_cafe():

    cafes = Cafe.query.all()
    cafe = choice(cafes)

    print(cafe)
    print(cafe.id)

    return jsonify({
        "cafe": {
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
            "has_sockets": cafe.has_sockets,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "id": cafe.id,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "map_url": cafe.map_url,
            "name": cafe.name,
            "seats": cafe.seats
        }
    })


# GET all cafe
@app.route("/all")
def get_all_cafe():
    cafes = Cafe.query.all()

    cafe_list = []

    for cafe in cafes:
        data = {
            "id": cafe.id,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
            "has_sockets": cafe.has_sockets,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "map_url": cafe.map_url,
            "name": cafe.name,
            "seats": cafe.seats
            }

        cafe_list.append(data)

    return jsonify({"cafes": cafe_list})


# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
