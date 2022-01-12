"""
* 구현
 - DEBUG /companies/candidates GET 예외 처리
    1. data invalid error
        (1) search_name 유효하지 않은 경우
    2. db can not access error
    3. interal server error

* 앞으로 할 일
 - TODO REFACTOR 코드 분리, 구조 개편
    1. req, res 객체 분리
    2. validators에서 추상화 후 반영
    3. 폴더 구조 확장 및 개편
 - TODO DOCS 구현한 기능에서 비즈니스 로직 설명 -> domain/company의 readme로 작성
 - TODO EXTEN fulltext 기능 구현
"""
from flask import request
from flask_restx import Namespace, Resource

from ..entities import db

from ..use_cases import CandidateGetUseCase

from ....helpers import InvalidDataException, InvalidDBAccessException
from ..validators import validate_candidates_get_data, validate_db_session



CompanyCandidatesNameSpace = Namespace('CompanyCandidates')


@CompanyCandidatesNameSpace.route('/')
class CompaniyCandidatesController(Resource):
    def get(self):
        try:
            # 예외 처리
            validate_candidates_get_data(request.args)  #1
            validate_db_session(db.session) #2

            search_name= request.args.get('search_name')
            # tags= request.args.get('')
            
            use_case = CandidateGetUseCase()
            response_data = use_case.execute(search_name)
            
            return response_data, 200

        except InvalidDataException as e:
            return "INVALID DATA EXCEPTION : "+e.code, 400

        except InvalidDBAccessException as e:
            return "INVALID DB ACCESS EXCEPTION : "+e.code, 500

        except Exception as e:
            return "INTERNAL SERVER ERROR : "+str(e)[:50], 500
        
    
