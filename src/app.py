import json

from flask import request
from flask_restx import Api, Namespace, Resource

from . import create_app
from .domain.company.controllers import CompanyNameSpace, CompanyCandidatesNameSpace

app = create_app()
api = Api(app)

api.add_namespace(CompanyNameSpace, '/companies')
api.add_namespace(CompanyCandidatesNameSpace, '/companies/candidates')
