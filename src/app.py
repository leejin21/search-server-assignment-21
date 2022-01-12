import json

from flask import request
from flask_restx import Api, Namespace, Resource

from . import create_app
from .domain.cat.controllers import CatNS
from .domain.company.controllers.company_controller import CompanyNameSpace
from .domain.company.controllers.candidate_controller import CompanyCandidatesNameSpace

app = create_app()
api = Api(app)

api.add_namespace(CatNS, '/cats')
api.add_namespace(CompanyNameSpace, '/companies')
api.add_namespace(CompanyCandidatesNameSpace, '/companies/candidates')
