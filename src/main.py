"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, People
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/users', methods=['GET'])
def handle_users():
    # get all the people
    people_query = User.query.all()
    all_people = list(map(lambda x: x.serialize(), people_query))

    return jsonify({
        "result": all_people
    }), 200


@app.route('/users/<int:id_user>/favs', methods=['GET'])
def obtener_favoritos(id_user):

    response_people = User.query.filter_by(id=id_user).first().peopleFav
    response_planets = User.query.filter_by(id=id_user).first().planetsFav
    People = list(map(lambda x: x.serialize(), response_people))
    Planets = list(map(lambda x: x.serialize(), response_planets))

    return jsonify({
        "PeopleFav": People,
        "PlanetsFav": Planets
    }), 200


@app.route('/favs/people/<int:people_id>', methods=['POST'])
def add_people_fav(people_id):
    id_user = 1
    user = User.query.get(id_user)
    character = People.query.get(people_id)
    print(id_user)
    listaFavoritos = User.query.filter_by(id=id_user).first().peopleFav
    listaFavoritos.append(character)
    db.session.commit()

    return jsonify({
        "success": "favorite added",
        "PeopleFav": list(map(lambda x: x.serialize(), listaFavoritos))
    }), 200


@app.route('/favs/people/<int:people_id>', methods=['DELETE'])
def remove_character_fav(people_id):
    id_user = 1
    user = User.query.get(id_user)
    character = People.query.get(people_id)
    listaFavoritos = User.query.filter_by(id=id_user).first().peopleFav
    listaFavoritos.remove(character)
    db.session.commit()

    return jsonify({
        "success": "favorite deleted",
        "PlanetsFav": list(map(lambda x: x.serialize(), listaFavoritos))
    }), 200


@app.route('/favs/planets/<int:planets_id>', methods=['POST'])
def add_planet_fav(planets_id):
    id_user = 1
    user = User.query.get(id_user)
    planet = Planets.query.get(planets_id)
    listaFavoritos = User.query.filter_by(id=id_user).first().planetsFav
    listaFavoritos.append(planet)
    db.session.commit()

    return jsonify({
        "success": "favorite added",
        "PlanetsFav": list(map(lambda x: x.serialize(), listaFavoritos))
    }), 200


@app.route('/favs/planets/<int:planets_id>', methods=['DELETE'])
def remove_planet_fav(planets_id):
    id_user = 1
    user = User.query.get(id_user)
    planet = Planets.query.get(planets_id)
    listaFavoritos = User.query.filter_by(id=id_user).first().planetsFav
    listaFavoritos.remove(planet)
    db.session.commit()
    return jsonify({
        "success": "favorite deleted",
        "PlanetsFav": list(map(lambda x: x.serialize(), listaFavoritos))
    }), 200


@app.route('/people', methods=['GET'])
def obtain_people():
    people_query = People.query.all()
    all_people = list(map(lambda x: x.serialize(), people_query))
    return jsonify({
        "result": all_people
    }), 200


@app.route('/people/<int:character_id>', methods=['GET'])
def obtain_details_character(character_id):
    character_query = People.query.get(character_id)
    data_character = character_query.serialize()
    return jsonify({
        "result": data_character
    }), 200


@app.route('/planets', methods=['GET'])
def obtain_planets():
    planets_query = Planets.query.all()
    all_planets = list(map(lambda x: x.serialize(), planets_query))
    response_body = {
        "result": all_planets
    }
    return jsonify(response_body), 200


@app.route('/planets/<int:planet_id>', methods=['GET'])
def obtener_detalles_planet(planet_id):
    planet_query = Planets.query.get(planet_id)
    data_planet = planet_query.serialize()
    response_body = {
        "result": data_planet
    }
    return jsonify(response_body), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
