
""" [Mission 2. 이메일 형식 체크 함수 만들기] Hanna 22/02/21

    - check_email_fmt 함수 : 이메일 형식 유효성 체크

    [1] check_email_fmt 함수 파라미터
        - 'email: str' : 형식을 체크할 이메일
        - return : 유효성 여부 True/False 반환
"""

import re


# 이메일은 계정@도메인.최상위도메인 형식. 계정에 [+-_.] 등의 문자가 들어갈 수 있음.
# 도메인에 [-] 문자를 사용할 수 있고, 최상위 도메인이 여러 단계일 수 있음.
def check_email_fmt(email: str) -> bool:

    regex = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    valid = re.match(regex, email)
    print(valid)
    if not valid:
        return False
    else:
        return True


# 테스트 코드
if __name__ == '__main__':
    emails = ["email@email.com", "email@email..com"]
    for e in emails:
        print(check_email_fmt(e))


