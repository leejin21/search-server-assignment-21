
from flask import request

from flask_restx import Api, Namespace, Resource

from . import repositories
from .entities import Companies, CompanyNames, Tags, CompanyTags
from .entities import db

CompanyNameSpace = Namespace('Companies')
CompanyCandidatesNameSpace = Namespace('CompaniyCandidates')

@CompanyNameSpace.route('/')
class CompaniesController(Resource):
    def get(self):
        return {}, 200

    def post(self):
        data = request.get_json()
        
        # Company 설정하기
        company = Companies()
        company_names = []

        # CompanyNames 설정하기
        for company_name in data['name_info']:
            lang = company_name['lang']
            name = company_name['name']
            company_names.append(CompanyNames(lang=lang, name=name))

        company.names = company_names

        # CompanyTags 설정하기
        company_tags = []
        for company_tag in data['tag_info']:
            lang = company_name['lang']
            for name in company_tag['tags']:
                company_tags.append(Tags(lang=lang, name=name))
        
        company.tags = company_tags
        
        # 세션 add
        db.session.add(company)
        db.session.add_all(company_names)
        db.session.add_all(company_tags)

        # 커밋
        db.session.commit()
        
        return data, 200


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
