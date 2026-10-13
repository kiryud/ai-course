def convert(value_str, from_unit, to_unit):
    # 1. 숫자 유효성 검사
    try:
        val = float(value_str)
    except ValueError:
        return "", "숫자를 입력해주세요"

    # 단위 그룹 정의
    length_units = {"mm", "cm", "m", "km"}
    temp_units = {"°C", "°F"}

    # 2. 단위 호환성 검사
    is_from_length = from_unit in length_units
    is_from_temp = from_unit in temp_units
    is_to_length = to_unit in length_units
    is_to_temp = to_unit in temp_units

    if (is_from_length and is_to_temp) or (is_from_temp and is_to_length):
        return "", "길이와 온도는 변환할 수 없습니다"
    
    if not (is_from_length or is_from_temp or is_to_length or is_to_temp):
        # 만약 정의되지 않은 단위가 들어온 경우 (확장성 대비)
        return "", "알 수 없는 단위입니다"

    # 3. 변환 로직
    result = val

    # --- 길이 변환 (기준: m) ---
    if is_from_length and is_to_length:
        # [from_unit] -> m
        to_meter_map = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0}
        meters = val * to_meter_map[from_unit]
        
        # m -> [to_unit]
        from_meter_map = {"mm": 1000.0, "cm": 100.0, "m": 1.0, "km": 0.001}
        result = meters * from_meter_map[to_unit]

    # --- 온도 변환 ---
    elif is_from_temp and is_to_temp:
        if from_unit == to_unit:
            result = val
        elif from_unit == "°C" and to_unit == "°F":
            result = (val * 9/5) + 32
        elif from_unit == "°F" and to_unit == "°C":
            result = (val - 32) * 5/9
    
    else:
        # 동일 단위인 경우 (예: m -> m)
        if from_unit == to_unit:
            result = val
        else:
            return "", "단위 변환 오류"

    return str(result), ""

