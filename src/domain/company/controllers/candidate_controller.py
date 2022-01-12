"""
* 구현
 - FEAT /companies/candidates GET 구현
    [비즈니스 로직]
    0. 띄어쓰기를 구분자로 split해서 S = s1 + s2 + s3 + ...로 만들어준다
    이후 S, s1, s2, s3로 차례로 아래 과정 1,2를 거친다.
    1. 첫 글자부터 일치하는 걸 먼저 찾는다
    2. 1도 없으면 중간부터 일치하는 걸 찾는다
    3. 모든 S, s1, s2, ... 부터 다 1,2과정을 거쳤는데도 없으면 빈 리스트 보낸다
    
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
from sqlalchemy import select
from flask_restx import Api, Namespace, Resource

from ..entities import db

from ..use_cases.candidate_get_use_case import CandidateGetUseCase

from ..exceptions import InvalidDataException, InvalidDBAccessException
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
        
    