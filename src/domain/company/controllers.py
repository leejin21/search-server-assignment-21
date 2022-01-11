
from flask import request

from flask_restx import Api, Namespace, Resource

from . import repositories
from .entities import Companies, CompanyNames, Tags, CompanyTags

CompanyNameSpace = Namespace('Companies')
CompanyCandidatesNameSpace = Namespace('CompaniyCandidates')

@CompanyNameSpace.route('/')
class CompaniesController(Resource):
    def get(self):
        pass
        return {}, 200

    def post(self):
        repositories.add_instance(Companies)
        return "Added", 200


@CompanyCandidatesNameSpace.route('/')
class CompanyCandidatesController(Resource):
    def get(self):
        companies = repositories.get_all(Companies)

        all_companies = []
        for comp in companies:
            new_comp = {
                "id": comp.id
            }
            all_companies.append(new_comp)

        return all_companies, 200
