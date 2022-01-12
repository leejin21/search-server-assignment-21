"""
* 앞으로 할 일
- TODO REFACTOR
    예외클래스 추상화: utils로 옮기기
    에러 코드 딕셔너리 생성, {code: msg} 꼴로 파일 만들기
    구조 개편
"""
class MainException(Exception):
    def __init__(self, code):
        self.code = code

class InvalidDataException(MainException):
    pass

class InvalidDBAccessException(MainException):
    pass

class DataNotExistException(MainException):
    pass
