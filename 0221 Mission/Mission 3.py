""" [Mission 3. 엑셀 <-> DB 함수 만들기] Hanna 22/02/22

    - 목표1 : 엑셀 파일을 읽어서 DB 테이블에 저장
    - 목표2 : 반대로 DB 테이블을 읽어서 엑셀로 저장

    [1] xlsx_to_db 함수
        - return : 성공 여부

    [2] db_to_xlsx 함수
        - return : 성공 여부
"""


def xlsx_to_db(fname: str) -> bool:
    """ fname.xlsx 엑셀 파일을 읽어서 DB 테이블에 저장 """
    pass
    return True


def xlsx_to_db(fname: str) -> bool:
    """ DB 테이블을 읽어서 fname.xlsx 엑셀 파일에 저장 """
    pass
    return True


# 테스트 코드
if __name__ == '__main__':
    fnames = ["email@email.com", "email@email..com",
              "em.a.il@email.co.kr", "dan@[128.6.3.40]"]
    for i, e in enumerate(fnames):
        print(f"[{i}]", check_email_fmt(fnames))
