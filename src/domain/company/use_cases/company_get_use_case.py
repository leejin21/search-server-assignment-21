"""
* 앞으로 할 일
- TODO lang: EN, KR, JP 또는 언어 약자들 중 하나로 포맷해야 함(유효성 검사)
"""
from ..repositories import CompanyRepository, TagRepository
from ....helpers import DataNotExistException



class CompanyGetUseCase:
    def __init__(self):
        pass

    def execute(self, lang, company_name):
        # 1. company.id 찾기
        result = CompanyRepository.search_by_name(name=company_name)
        if not result:
            raise DataNotExistException('company name invalid')
        else:
            company = result.Company
        
        # 2. 해당하는 company가 보유하는 태그 리스트 찾기
        tag_list = TagRepository.search_tags_by_company_name(lang=lang, name=company_name)

        return {"id":company.id, "tag_info": tag_list, "name": company_name}
        