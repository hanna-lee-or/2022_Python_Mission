
""" [Mission 1. 시간 값 변환 함수 만들기] Hanna 22/02/21

    - 파라미터에 따라 현재 시간 정보를 특정 포맷으로 Print 합니다.
    - (((  여기 주석은 함수 작성 완료하고 수정하기  )))

    [1] 파라미터는 총 3개
        - 현재 시각 now
        - 시간 출력 포맷 string
        - 시간대 타입 UTC/KST (default = KST)
    [2] 만들어야 할 함수는 총 2개
        - UTC → KST 변환 함수 1개
        - 변환 함수를 이용한 시간 정보 출력 함수 1개
"""

import time
from datetime import datetime, timezone, timedelta


# datetime(UTC) -> datetime(KST) 변환.
def utc_to_kst(t: datetime) -> datetime:
    kst = timezone(timedelta(hours=9))
    return t.astimezone(kst)


# datetime -> Format String 에 맞춰 변환
def time_to_fstr(t: datetime, fmt: str) -> str:
    fmt = fmt.replace('YYYY', '%Y')
    fmt = fmt.replace('yy', '%y')
    fmt = fmt.replace('mm', '%m')     # 월
    fmt = fmt.replace('dd', '%d')     # 일
    fmt = fmt.replace('ll', '%l')     # 12시간제 시간
    fmt = fmt.replace('HH', '%H')     # 24시간제 시간
    fmt = fmt.replace('MM', '%M')     # 분
    fmt = fmt.replace('SS', '%S')     # 초
    return t.strftime(fmt)


# 현재 시간 정보(UTC 기준)를 지정된 시간대, 출력 포맷으로 변환
def trans_time(t: datetime, fmt: str, time_zone: str = 'KST') -> str:

    # t 유효성 체크
    if not isinstance(t, datetime):
        return 'Wrong time (not datetime)'

    # time_zone 유효성 체크
    time_zone = time_zone.upper()
    if time_zone not in ['KST', 'UTC']:
        return 'Wrong time_zone (not KST/UTC)'

    # [1] time_zone 이 KST 인 경우 UTC -> KST 변환
    if time_zone == 'KST':
        t = utc_to_kst(t)

    # [2] fmt 포맷에 맞게 시간 정보 변환
    trans_t = time_to_fstr(t, fmt)

    return trans_t


# 테스트 코드
if __name__ == '__main__':
    # 현재 시각(UTC)를 기준으로 테스트
    now = datetime.now(timezone.utc)
    # 테스트할 포맷들
    ftz = [('YYYY-mm-dd HH:MM:SS', 'KST'), ('yy년 mm월 dd일', 'error'),
         ('현재 MM분 SS초 입니다.', 'UTC'), ('mm 월 MM 분', 'kst'), ('-', 'utc')]
    # 현재 시간 정보(UTC 기준)를 지정된 시간대, 출력 포맷으로 변환
    for i in range(len(ftz)):
        print(f"[{i}]", trans_time(now, ftz[i][0], ftz[i][1]))

