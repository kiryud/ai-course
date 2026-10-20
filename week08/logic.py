from datetime import datetime

def calculate_parking_fee(entry_str: str, exit_str: str):
    """
    입차 시각과 출차 시각을 받아 주차 시간과 요금을 계산합니다.
    
    Args:
        entry_str (str): 입차 시각 (HH:MM)
        exit_str (str): 출차 시각 (HH:MM)
        
    Returns:
        tuple: (duration_str, fee)
            - duration_str (str): 주차 시간 (예: "1시간 30분")
            - fee (int): 계산된 요금
            
    Raises:
        ValueError: 시간이 유효하지 않거나 출차 시간이 입차 시간보다 빠를 경우
    """
    fmt = "%H:%M"
    try:
        t1 = datetime.strptime(entry_str, fmt)
        t2 = datetime.strptime(exit_str, fmt)
    except ValueError:
        raise ValueError("시간 형식이 올바르지 않습니다. (HH:MM)")

    if t2 <= t1:
        raise ValueError("출차 시간은 입차 시간보다 늦어야 합니다.")

    diff = t2 - t1
    total_seconds = diff.seconds
    total_minutes = total_seconds // 60
    
    # 주차 시간 문자열 계산
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    duration_str = f"{h}시간 {m}분"

    # 요금 규칙 적용
    # 30분까지 무료, 이후 10분마다 500원 (올림), 하루 최대 20,000원
    if total_minutes <= 30:
        fee = 0
    else:
        extra_minutes = total_minutes - 30
        # 10분 단위 올림 처리 (예: 1분이라도 있으면 10분으로 간주)
        units = (extra_minutes + 9) // 10
        fee = min(units * 500, 20000)
    
    return duration_str, fee