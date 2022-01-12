from .repositories import CompanyRepository, CompanyNameRepository, TagRepository
from .repositories import db_add, db_add_all, db_commit

class CompanyPostUseCase:
    def __init__(self):
        pass

    def execute(self, data):
        # Company 설정하기
        company = CompanyRepository.init_instance()
        company_names = []

        # CompanyNames 설정하기
        # TODO 1줄로 줄이기
        for company_name in data['name_info']:
            lang = company_name['lang']
            name = company_name['name']
            instance = CompanyNameRepository.init_instance(lang=lang, name=name)
            company_names.append(instance)

        company.names = company_names

        # CompanyTags 설정하기
        exist_tags = []; not_exist_tags = []
        for company_tag in data['tag_info']:
            lang = company_name['lang']
            for name in company_tag['tags']:    
                # 이미 존재하는 tag의 경우 해당 태그로 CompanyTags 테이블에 저장
                tag = TagRepository.search_by_name(name)
                if tag:
                    exist_tags.append(tag)
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
        