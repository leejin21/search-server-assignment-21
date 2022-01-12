"""
* 앞으로 할 일
- TODO REFACTOR
    DB-validator, req-object-validator 분리하기
    추상화, 구조 개편
"""
from ..exceptions import InvalidDataException



def validate_companies_get_data(params):
    # 예외 처리 1. data invalid error
    # (1) company_name 길이가 0이거나, 없는 경우
    if not params.get('company_name'):
        raise InvalidDataException("invalid query: company_names not exist")
    # (2) lang 길이가 0이거나, 없는 경우
    if not params.get('lang'):
        raise InvalidDataException("invalid query: lang not exist")
    
    return False


def validate_companies_post_data(data):
    # 예외 처리 1. data invalid error
    # (1) name_info 길이가 0일 경우
    if len(data['name_info']) == 0:
        raise InvalidDataException("invalid name_info: name_info length == 0")

    # (2) name_info.name 길이가 0일 경우
    for cn in data['name_info']:
        if len(cn['name']) == 0:
            raise InvalidDataException("invalid name_info: names legnth == 0")

    # (3) tag_info.tags 길이가 0일 경우
    for tag in data['tag_info']:
        if len(tag['tags']) == 0:
            raise InvalidDataException("invalid tag_info: tags length == 0")
    
    return False
