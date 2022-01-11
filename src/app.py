import json

from flask import request
from flask_restx import Api, Namespace, Resource

from . import create_app, database
from .models import Cats

app = create_app()
api = Api(app)

CatNS = Namespace('Cats')
api.add_namespace(CatNS, '/cats')

# @app.route('/cat/', methods=['GET'])
@CatNS.route('/')
class CatsGet(Resource):
    def get(self):
        cats = database.get_all(Cats)
        all_cats = []
        for cat in cats:
            new_cat = {
                "id": cat.id,
                "name": cat.name,
                "price": cat.price,
                "breed": cat.breed
            }

            all_cats.append(new_cat)
        return all_cats, 200


@app.route('/cat/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    price = data['price']
    breed = data['breed']

    database.add_instance(Cats, name=name, price=price, breed=breed)
    return json.dumps("Added"), 200


@app.route('/cat/remove/<cat_id>', methods=['DELETE'])
def remove(cat_id):
    database.delete_instance(Cats, id=cat_id)
    return json.dumps("Deleted"), 200


@app.route('/cat/edit/<cat_id>', methods=['PATCH'])
def edit(cat_id):
    data = request.get_json()
    new_price = data['price']
    database.edit_instance(Cats, id=cat_id, price=new_price)
    return json.dumps("Edited"), 200