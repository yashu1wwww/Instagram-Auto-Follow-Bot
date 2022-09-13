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

    return jsonify({
        "a length": len(cafe_list),
        "cafes": cafe_list
    })


#   SEARCH
@app.route("/search")
def search():
    query = request.args.get("loc")

    print(query)

    # ##################################################
    #   GET SINGLE FIRST RESULT
    # cafe = Cafe.query.filter_by(location=query).first()
    # return jsonify({"cafe": cafe})

    cafes = Cafe.query.filter_by(location=query).all()
    cafe_list = []

    for cafe in cafes:
        data = {
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

        cafe_list.append(data)

    if len(cafe_list) == 0:
        return jsonify({"error": {
            "Not Found": "Sorry, we don't have a cafe at that location."
        }})

    return jsonify({
        "length": len(cafe_list),
        "cafe": cafe_list
    })


#   HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    data = request.json
    print(data)
    print(data["name"])

    new_cafe = Cafe(
        name=data["name"],
        map_url=data["map_url"],
        img_url=data["img_url"],
        location=data["location"],
        seats=data["seats"],
        has_toilet=data["has_toilet"],
        has_wifi=data["has_wifi"],
        has_sockets=data["has_sockets"],
        can_take_calls=data["can_take_calls"],
        coffee_price=data["coffee_price"]
    )

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify({
        "response": {
            "success": "Successfully add new cafe."
        }
    })


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    price = request.args.get("coffee_price")

    if cafe:
        cafe.coffee_price = f"£{price}"
        db.session.add(cafe)
        db.session.commit()
        return jsonify({"success": "Successfully update cafe price"})
    else:
        return jsonify({"error": {"Not Found": "Sorry a cafe with that id was not found in the database."}})


# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
