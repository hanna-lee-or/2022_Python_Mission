""" [Mission 2. 이메일 형식 체크 함수 만들기] Hanna 22/02/21

    - 목표 : 이메일 형식 유효성 체크

    [1] check_email_fmt 함수
        - return : 유효성 여부 True/False 반환
"""

import re


# 이메일은 계정@도메인.최상위도메인 형식. 계정에 [+-_.] 등의 문자가 들어갈 수 있음.
# 도메인에 [-] 문자를 사용할 수 있고, 최상위 도메인이 여러 단계일 수 있음.
def check_email_fmt(email: str) -> bool:
    """ 이메일 형식 유효성 체크 """
    regex = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+' \
            '@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    valid = re.fullmatch(regex, email)
    if not valid:
        return False
    else:
        return True


# 테스트 코드
if __name__ == '__main__':
    emails = ["email@email.com", "email@email..com",
              "em.a.il@email.co.kr", "dan@[128.6.3.40]"]
    for i, e in enumerate(emails):
        print(f"[{i}]", check_email_fmt(e))
