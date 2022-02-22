""" [Mission 3. 엑셀 <-> DB 함수 만들기] Hanna 22/02/22

    - 목표1 : 엑셀 파일을 읽어서 DB 테이블에 저장
    - 목표2 : 반대로 DB 테이블을 읽어서 엑셀로 저장

    [1] xlsx_to_db 함수
        - return : 성공 여부

    [2] db_to_xlsx 함수
        - return : 성공 여부
"""

# pip install pymysql, pandas
import pandas as pd
import pymysql


def xlsx_to_db(fname: str) -> bool:
    """ fname.xlsx 엑셀 파일을 읽어서 DB 테이블에 저장 """

    return True


def db_to_xlsx(fname: str) -> bool:
    """ DB 테이블을 읽어서 fname.xlsx 엑셀 파일에 저장 """

    return True


# 테스트 코드
if __name__ == '__main__':
    fnames = ("서울도서관 분야별 장서현황_지식문화과", "DB 장서현황")
    print(f"[{fnames[0]} -> DB]", xlsx_to_db(fnames[0]))
    print(f"[DB -> {fnames[1]}]", db_to_xlsx(fnames[1]))
