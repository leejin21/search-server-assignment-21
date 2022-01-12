"""
* 구현


* 앞으로 할 일
 - TODO FEAT /companies/candidates GET 구현
 - TODO DEBUG /companies/candidates GET 예외 처리
    1. data invalid error
    2. db can not access error
    3. data already exist error
    4. interal server error
 - TODO REFACTOR use_cases, repositories로 분리
 - TODO REFACTOR 코드 분리, 구조 개편
    1. req, res 객체 분리
    2. validators에서 추상화 후 반영
    3. 폴더 구조 확장 및 개편
 - TODO DOCS 구현한 기능에서 비즈니스 로직 설명 -> domain/company의 readme로 작성

"""
from flask import request
from sqlalchemy import select
from flask_restx import Api, Namespace, Resource

from ..entities import Companies, CompanyNames, Tags, CompanyTags
from ..entities import db

from ..use_cases.company_post_use_case import CompanyPostUseCase

from ..exceptions import InvalidDataException, InvalidDBAccessException
from ..validators.company_validators import validate_companies_post_data, validate_db_session

CompanyCandidatesNameSpace = Namespace('CompanyCandidates')

@CompanyCandidatesNameSpace.route('/')
class CompaniyCandidatesController(Resource):
    def get(self):
        try:
            search_name= request.args.get('search_name')
            # tags= request.args.get('')
            
            
            return {}, 200
        except Exception as e:
            return "INTERNAL SERVER ERROR : "+str(e)[:50], 500
        
    