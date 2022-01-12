"""
* 앞으로 할 일
- TODO FEAT 자동완성 기능 구현
    1. sub_string으로 검색
    2. 비즈니스 로직 짜기
    3. 예외처리
"""

from ..repositories import CompanyNameRepository

class CandidateGetUseCase:
    def __init__(self):
        pass

    def execute(self, search_name):
        # 서치할 단어들 => S s1 s2 s3 ...(우선순위 부여)
        search_name_list = [search_name] + search_name.split(' ')

        for search_string in search_name_list:
            # 1. TRY 첫 글자부터 일치하는 걸 찾음
            front_results = CompanyNameRepository.search_by_substring_front(search_string)

            if front_results:
                candidate_list = [row['CompanyNames'].name for row in front_results]
                return {"candidates": candidate_list}
            
            # 2. TRY 중간 글자부터 일치하는 걸 찾음
            middle_results = CompanyNameRepository.search_by_substring_middle(search_string)
            
            if middle_results:
                candidate_list = [row['CompanyNames'].name for row in middle_results]
                return {"candidates": candidate_list}

        return {"candidates": []}
        