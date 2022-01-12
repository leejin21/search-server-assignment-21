"""
* 구현
 - FEAT /companies/ POST 구현
 - DEBUG /companies/ POST : tags 찾아서 연결하기, 없는 경우 생성하기
 - DEBUG /companies/ POST 예외 처리
    1. data invalid error
        (1) name_info 길이가 0일 경우
        (2) name_info.name 길이가 0일 경우
        (3) tag_info.tags 길이가 0일 경우
    2. db can not access error
    3. data already exist error
        (1) name_info.name이 기존 DB에 있는 name과 겹치는 경우
    4. interal server error
- REFACTOR use_cases, repositories로 분리


* 앞으로 할 일
 - TODO REFACTOR 코드 분리, 구조 개편
    1. req, res 객체 분리
    2. validators에서 추상화 후 반영
    3. 폴더 구조 확장 및 개편
 - TODO DOCS 구현한 기능에서 비즈니스 로직 설명 -> domain/company의 readme로 작성

"""
from flask import request
from sqlalchemy import select
from flask_restx import Api, Namespace, Resource

from .entities import Companies, CompanyNames, Tags, CompanyTags
from .entities import db

from .use_cases import CompanyPostUseCase

from .exceptions import InvalidDataException, InvalidDBAcessException
from .validators import validate_companies_post_data, validate_companyname_already_exists, validate_db_session

CompanyNameSpace = Namespace('Companies')
CompanyCandidatesNameSpace = Namespace('CompaniyCandidates')

@CompanyNameSpace.route('/')
class CompaniesController(Resource):
    def get(self):
        return {}, 200

    def post(self):
        try:
            data = request.get_json()

            # * 예외 처리
            validate_companies_post_data(data) # 1
            validate_db_session(db.session) # 2
            validate_companyname_already_exists(data, select, db.session, CompanyNames) # 3

            # * 유스케이스 생성해 반영
            use_case = CompanyPostUseCase()
            response_data = use_case.execute(data)
            
            return response_data, 200

        except InvalidDataException as e:
            return "INVALID DATA EXCEPTION : "+e.code, 400

        except InvalidDBAcessException as e:
            return "INVALID DB ACCESS EXCEPTION : "+e.code, 500

        except Exception as e:
            return "INTERNAL SERVER ERROR : "+str(e)[:50], 500
        

# @CompanyCandidatesNameSpace.route('/')
# class CompanyCandidatesController(Resource):
#     def get(self):
#         companies = repositories.get_all(Companies)

#         all_companies = []
#         for comp in companies:
#             new_comp = {
#                 "id": comp.id
#             }
#             all_companies.append(new_comp)

#         return all_companies, 200
