import json
from logging import captureWarnings

from flask import request

from flask_restx import Api, Namespace, Resource

from . import repositories
from .entities import Cats


CatNS = Namespace('Cats')


@CatNS.route('/')
class CatsGet(Resource):
    def get(self):
        cats = repositories.get_all(Cats)
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
    
    def post(self):
        data = request.get_json()
        name = data['name']
        price = data['price']
        breed = data['breed']

        repositories.add_instance(Cats, name=name, price=price, breed=breed)
        return "Added", 200

    def delete(self):
        id= request.args.get('id')
        repositories.delete_instance(Cats, id=id)
        return "Deleted", 200


# @CatNS.route('/')
# class CatsRemove(Resource):

