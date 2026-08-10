from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, select
import random, os

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "instance", "cafes.db")
db_uri = "sqlite:///" + os.path.abspath(db_path).replace("\\", "/")
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe = {
            "name" : random_cafe.name,
            "map_url" : random_cafe.map_url,
            "img_url" : random_cafe.img_url,
            "location" : random_cafe.location,
            "has_sockets" : random_cafe.has_sockets,
            "has_wifi" : random_cafe.has_wifi,
            "can_take_calls" : random_cafe.can_take_calls,
            "seats" : random_cafe.seats,
            "coffee_price" : random_cafe.coffee_price
        }), 200

@app.route("/all")
def all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(cafes = [{
                "name" : cafe.name,
                "map_url" : cafe.map_url,
                "img_url" : cafe.img_url,
                "location" : cafe.location,
                "has_sockets" : cafe.has_sockets,
                "has_wifi" : cafe.has_wifi,
                "can_take_calls" : cafe.can_take_calls,
                "seats" : cafe.seats,
                "coffee_price" : cafe.coffee_price
            } for cafe in all_cafes]), 200

@app.route("/search")
def search_cafe():
    location = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    filtered_cafes = result.scalars().all()
    return jsonify(cafes = [{
                    "name" : cafe.name,
                    "map_url" : cafe.map_url,
                    "img_url" : cafe.img_url,
                    "location" : cafe.location,
                    "has_sockets" : cafe.has_sockets,
                    "has_wifi" : cafe.has_wifi,
                    "can_take_calls" : cafe.can_take_calls,
                    "seats" : cafe.seats,
                    "coffee_price" : cafe.coffee_price
                } for cafe in filtered_cafes]), 200

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."}), 200

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    result_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id))
    cafe = result_cafe.scalar_one()
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key != "TopSecretAPIKey":
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

    try:
        cafe_id_int = int(cafe_id)
    except ValueError:
        return jsonify(error={"Bad Request": "Sorry, that cafe id is invalid."}), 400

    cafe = db.session.get(Cafe, cafe_id_int)
    if cafe is None:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200


if __name__ == '__main__':
    app.run(debug=True)
