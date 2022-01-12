"""
* 구현
 - FEAT /companies/candidates GET 구현
    [비즈니스 로직]
    0. 띄어쓰기를 구분자로 split해서 S = s1 + s2 + s3 + ...로 만들어준다
    이후 S, s1, s2, s3로 차례로 아래 과정 1,2를 거친다.
    1. 첫 글자부터 일치하는 걸 먼저 찾는다
    2. 1도 없으면 중간부터 일치하는 걸 찾는다
    3. 모든 S, s1, s2, ... 부터 다 1,2과정을 거쳤는데도 없으면 빈 리스트 보낸다

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
                candidate_list = [row['CompanyName'].name for row in front_results]
                return {"candidates": candidate_list}
            
            # 2. TRY 중간 글자부터 일치하는 걸 찾음
            middle_results = CompanyNameRepository.search_by_substring_middle(search_string)
            
            if middle_results:
                candidate_list = [row['CompanyName'].name for row in middle_results]
                return {"candidates": candidate_list}

        return {"candidates": []}
        