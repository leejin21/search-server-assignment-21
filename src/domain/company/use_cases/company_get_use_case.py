"""
* 앞으로 할 일
- TODO lang: EN, KR, JP 중 하나로 포맷해야 함(유효성 검사)
"""
from ..repositories import CompanyRepository, TagRepository
from ..exceptions import DataNotExistException



class CompanyGetUseCase:
    def __init__(self):
        pass

    def execute(self, lang, company_name):
        # Company JOIN CompanyNames JOIN CompanyTags 찾기
        
        result = CompanyRepository.search_by_name(name=company_name)
        if not result:
            raise DataNotExistException('company name invalid')
        else:
            company = result.Companies
        
        tag_list = TagRepository.search_tags_by_company_name(lang=lang, name=company_name)
        if not tag_list:
            raise DataNotExistException('company name or lang invalid')

        return {"id":company.id, "tag_info": tag_list, "name": company_name}
        