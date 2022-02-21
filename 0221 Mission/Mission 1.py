
""" [Mission 1. 시간 값 변환 함수 만들기] Hanna 22/02/21

    - trans_time 함수 : 파라미터에 따라 현재 시간 정보를 특정 포맷으로 Print

    [1] trans_time 함수 파라미터
        - 't: datetime' : 현재 시각 now
        - 'fmt: str' : 해당 문자열 포맷으로 시간 값 변환
        - 'tz: str' : 지정한 시간대 UTC/KST 타입으로 시간 값 변환 (default = KST)
        - return : 변환된 시간 문자열 반환

    [2] time_to_fstr 함수 파라미터
        - 't: datetime' : 변환할 시간 값
        - 'fmt: str' : 해당 문자열 포맷으로 시간 값 변환
        - return : 변환된 시간 문자열 반환

    [3] utc_to_kst 함수 파라미터
        - 't: datetime' : kst 시간대로 변환할 시간 값
        - return : kst 기준 시간 값 (datetime) 반환
"""

from datetime import datetime, timezone, timedelta


# datetime(UTC) -> datetime(KST)
def utc_to_kst(t: datetime) -> datetime:
    kst = timezone(timedelta(hours=9))
    kst_t = t.astimezone(kst)
    return kst_t


# datetime -> Format String 에 맞춰 변환
# strftime 함수는 '%_'(방식1) 문자열을 인식해 시간 정보를 변환한다.
# 'yyyy-mm-dd HH:MM:SS'(방식2) 형식으로 포맷을 지정하면
# (방식1)로 바꾸어 strftime 함수로 시간 정보를 변환하도록 구성.
def time_to_fstr(t: datetime, fmt: str) -> str:
    trans_table = {'yyyy': '%Y', 'yy': '%y',    # 년도
                   'mm': '%m', 'dd': '%d',      # 월 / 일
                   'll': '%l', 'HH': '%H',      # 12시간제 / 24시간제
                   'MM': '%M', 'SS': '%S'}      # 분 / 초
    for key in trans_table:
        fmt = fmt.replace(key, trans_table[key])
    trans_t = t.strftime(fmt)
    return trans_t


# 현재 시간 정보(UTC 기준)를 지정한 시간대, 출력 포맷으로 변환
def trans_time(t: datetime, fmt: str, tz: str = 'KST') -> str:

    # t 유효성 체크
    if not isinstance(t, datetime):
        return 'Wrong time (not datetime)'

    # time_zone 유효성 체크
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
    # 현재 시각(UTC)를 기준으로 테스트
    now = datetime.now(timezone.utc)
    # 테스트할 포맷들
    ftz = [('yyyy-mm-dd HH:MM:SS', 'KST'), ('yy년 mm월 dd일', 'error'),
           ('현재 SS초, MM분 SS초 입니다.', 'UTC'), ('mm 월 MM 분', 'kst'),
           ('%Y-%m-%d %H:%M:%S', 'utc'), ('-', 'utc')]
    # 현재 시간 정보(UTC 기준)를 지정된 시간대, 출력 포맷으로 변환
    for i in range(len(ftz)):
        print(f"[{i}]", trans_time(now, ftz[i][0], ftz[i][1]))

