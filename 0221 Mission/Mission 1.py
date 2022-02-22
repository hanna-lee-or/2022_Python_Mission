
""" [Mission 1. 시간 값 변환 함수 만들기] Hanna 22/02/21

    - 목표 : 파라미터에 따라 현재 시간 정보를 특정 포맷으로 Print

    [1] trans_time 함수
        - return : 변환된 시간 문자열 반환

    [2] time_to_fstr 함수
        - return : 변환된 시간 문자열 반환

    [3] utc_to_kst 함수
        - return : kst 기준 datetime 시간 값 반환
"""

from datetime import datetime, timezone, timedelta


def utc_to_kst(t: datetime) -> datetime:
    """ datetime(UTC) -> datetime(KST) """
    kst = timezone(timedelta(hours=9))
    kst_t = t.astimezone(kst)
    return kst_t


def time_to_fstr(t: datetime, fmt: str) -> str:
    """ datetime -> Format String 에 맞춰 변환 :
        (방식1) '%Y-%m-%d %H:%M:%S
        (방식2) 'yyyy-mm-dd HH:MM:SS'
        : 2가지 Format String 모두 지원
    """
    trans_table = {'yyyy': '%Y', 'yy': '%y',    # 년도
                   'mm': '%m', 'dd': '%d',      # 월 / 일
                   'll': '%l', 'HH': '%H',      # 12시간제 / 24시간제
                   'MM': '%M', 'SS': '%S'}      # 분 / 초
    for key in trans_table:
        fmt = fmt.replace(key, trans_table[key])
    trans_t = t.strftime(fmt)
    return trans_t


def trans_time(t: datetime, fmt: str, tz: str = 'KST') -> str:
    """ 현재 시간 정보(UTC 기준)를 지정한 시간대, 출력 포맷으로 변환 """

    # 파라미터 유효성 체크
    if not isinstance(t, datetime):
        return 'Wrong time (not datetime)'

    tz = tz.upper()
    if tz not in ['KST', 'UTC']:
        return 'Wrong time_zone (not KST/UTC)'

    # [1] time_zone 이 KST 인 경우 UTC -> KST 변환
    if tz == 'KST':
        t = utc_to_kst(t)

    # [2] fmt 포맷에 맞게 시간 정보 변환
    trans_t = time_to_fstr(t, fmt)

    return trans_t


# 테스트 코드
if __name__ == '__main__':
    now = datetime.now(timezone.utc)
    ftz = [('yyyy-mm-dd HH:MM:SS', 'KST'), ('yy년 mm월 dd일', 'error'),
           ('현재 SS초, MM분 SS초 입니다.', 'UTC'), ('mm 월 MM 분', 'kst'),
           ('%Y-%m-%d %H:%M:%S', 'utc'), ('-', 'utc')]
    for i in range(len(ftz)):
        print(f"[{i}]", trans_time(now, ftz[i][0], ftz[i][1]))

