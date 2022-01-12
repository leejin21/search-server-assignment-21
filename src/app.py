from flask_restx import Api

from . import create_app
from .domain.company.controllers import CompanyNameSpace, CompanyCandidatesNameSpace

app = create_app()
api = Api(app)

api.add_namespace(CompanyNameSpace, '/companies')
api.add_namespace(CompanyCandidatesNameSpace, '/companies/candidates')
