from .exceptions import InvalidDBAcessException, InvalidDataException

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

def validate_companyname_already_exists(result):
    # 예외 처리 2. data already exist error
    # (1) name_info.name이 기존 DB에 있는 name과 겹치는 경우
    if result:
        raise InvalidDataException('name_info.name already exist in CompanyNames')
