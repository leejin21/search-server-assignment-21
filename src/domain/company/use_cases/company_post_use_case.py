"""
* 앞으로 할 일
- TODO REFACTOR
    유즈케이스 추상화
    CompanyNames 설정 부분 한줄로 처리
    execute 메소드 -> company names, company tags 두 부분으로 분리
"""
from ..repositories import CompanyRepository, CompanyNameRepository, TagRepository
from ..repositories import db_add, db_add_all, db_commit
from ....helpers import InvalidDataException



class CompanyPostUseCase:
    def __init__(self):
        pass

    def execute(self, data):
        # Company 설정하기
        company = CompanyRepository.init_instance()
        company_names = []

        # CompanyNames 설정하기
        for company_name in data['name_info']:
            lang = company_name['lang']
            name = company_name['name']

            # 예외처리: company name이 이미 존재하는 지 검사
            result = CompanyNameRepository.search_by_name(name)
            if result:
                raise InvalidDataException('name_info.name already exist in CompanyNames')

            instance = CompanyNameRepository.init_instance(lang=lang, name=name)
            
            company_names.append(instance)

        company.names = company_names

        # CompanyTags 설정하기
        exist_tags = []; not_exist_tags = []
        for company_tag in data['tag_info']:
            lang = company_tag['lang']
            for name in company_tag['tags']:    
                # 이미 존재하는 tag의 경우 해당 태그로 CompanyTags 테이블에 저장
                result = TagRepository.search_by_name(name)
                if result:
                    exist_tags.append(result.Tag)
                else:
                    # 존재하지 않는 경우 해당 태그를 생성해 CompanyTags 테이블에 저장
                    instance = TagRepository.init_instance(lang=lang, name=name)
                    not_exist_tags.append(instance)

        company_tags = exist_tags + not_exist_tags
        company.tags = company_tags

        # DB에 추가하는 company 정보들 insert
        db_add(company)
        db_add_all(company_names)
        db_add_all(not_exist_tags)

        # DB에 커밋
        db_commit()

        return data
        