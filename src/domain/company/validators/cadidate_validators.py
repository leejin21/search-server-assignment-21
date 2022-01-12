"""
* 앞으로 할 일
- TODO DOCS
"""
from ..exceptions import InvalidDataException



def validate_candidates_get_data(params):
    # 예외 처리 1. data invalid error
        # (1) search_name 유효하지 않은 경우
    if not params.get('search_name'):
        raise InvalidDataException('search_name is missing')
    return False
