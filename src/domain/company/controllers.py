"""
* 구현
 - FEAT /companies/ POST 구현
 - DEBUG /companies/ POST : tags 찾아서 연결하기, 없는 경우 생성하기

* 앞으로 할 일
 - TODO DEBUG 예외 처리
    1. data invalid error
        (1) name_info 길이가 0일 경우
        (2) name_info.name 길이가 0일 경우
        (3) tags 테이블에 tag_info.tags 길이가 0일 경우
    2. db can not access error
 - TODO REFACTOR repositories, use_cases로 코드 분리
 - TODO DOCS 구현한 기능에서 비즈니스 로직 설명 -> domain/company의 readme로 작성

"""
from flask import request

from flask_restx import Api, Namespace, Resource

from . import repositories
from .entities import Companies, CompanyNames, Tags, CompanyTags
from .entities import db

from sqlalchemy import select

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
        exist_tags = []; not_exist_tags = []
        for company_tag in data['tag_info']:
            lang = company_name['lang']

            for name in company_tag['tags']:    
                # tag 찾기
                stmt = select(Tags).where(Tags.name==name)
                result = db.session.execute(stmt)
                tag = result.fetchone().Tags

                if tag:
                    exist_tags.append(tag)
                else:
                    not_exist_tags.append(Tags(lang=lang, name=name))

        company_tags = exist_tags + not_exist_tags
        company.tags = company_tags
        
        # 세션 add
        db.session.add(company)
        db.session.add_all(company_names)
        db.session.add_all(not_exist_tags)

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
