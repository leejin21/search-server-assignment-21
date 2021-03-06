"""
* 구현
 - DEBUG /companies/ POST 예외 처리
    1. data invalid error
        (1) name_info 길이가 0일 경우
        (2) name_info.name 길이가 0일 경우
        (3) tag_info.tags 길이가 0일 경우
        (4) lang이 비즈니스 로직에서 정의하지 않은 언어에 해당하는 경우 
    2. db can not access error
    3. data already exist error
        (1) name_info.name이 기존 DB에 있는 name과 겹치는 경우
    4. interal server error

- DEBUG /companies/ GET 예외 처리
    1. data invalid error
        (1) company_name 유효하지 않은 경우
        (2) lang 유효하지 않은 경우: 없거나, 길이 == 0이거나
        (3) lang이 비즈니스 로직에서 정의하지 않은 언어에 해당하는 경우 
    2. db can not access error
    3. data invalid error
        (1) company name이 테이블에 존재X
        (2) lang이 유효하지 않은 문자열일 경우 
    4. interal server error

* 앞으로 할 일
 - TODO REFACTOR 코드 분리, 구조 개편
    1. req, res 객체 분리
    2. validators에서 추상화 후 반영
    3. 폴더 구조 확장 및 개편
 - TODO DOCS 구현한 기능에서 비즈니스 로직 설명 -> domain/company의 readme로 작성

"""
from flask import request
from flask_restx import Namespace, Resource

from ..entities import db

from ..use_cases import CompanyPostUseCase, CompanyGetUseCase

from ....helpers import InvalidDataException, InvalidDBAccessException, DataNotExistException
from ..validators import validate_companies_post_data, validate_db_session, validate_companies_get_data



CompanyNameSpace = Namespace('Companies')


@CompanyNameSpace.route('/')
class CompaniesController(Resource):
    def get(self):
        try:
            # * 예외처리
            validate_companies_get_data(request.args) # 1
            validate_db_session(db.session) # 2

            company_name= request.args.get('company_name')
            lang = request.args.get('lang')
            
            # * 유스케이스 생성해 데이터 가져오기
            use_case = CompanyGetUseCase()
            response_data = use_case.execute(lang, company_name)
            
            return {"status": 200, "message": "", "response_data": response_data}, 200

        
        except InvalidDataException as e:
            return {"status": 400, "message": "INVALID DATA EXCEPTION : "+e.code}, 200

        except InvalidDBAccessException as e:
            return {"status": 500, "message": "INVALID DB ACCESS EXCEPTION : "+e.code}, 500
        
        except DataNotExistException as e:
            return {"status": 400, "message": "DATA NOT EXIST EXCEPTION : "+e.code}, 400

        except Exception as e:
            return {"status": 500, "message": "INTERNAL SERVER ERROR : "+str(e)[:50]}, 500
            

    def post(self):
        try:
            data = request.get_json()

            # * 예외 처리
            validate_companies_post_data(data) # 1
            validate_db_session(db.session) # 2

            # * 유스케이스 생성해 데이터 반영
            use_case = CompanyPostUseCase()
            response_data = use_case.execute(data)
            
            return {"status": 200, "message": "", "response_data": response_data}, 200

        except InvalidDataException as e:
            return {"status": 400, "message": "INVALID DATA EXCEPTION : "+e.code}, 200

        except InvalidDBAccessException as e:
            return {"status": 500, "message": "INVALID DB ACCESS EXCEPTION : "+e.code}, 500

        except Exception as e:
            return {"status": 500, "message": "INTERNAL SERVER ERROR : "+str(e)[:50]}, 500
        
    