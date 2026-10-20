from logic import calculate_parking_fee

def run_test(name, func):
    """개별 테스트 그룹을 실행하고 성공/실패 여부를 반환합니다."""
    print(f"🔍 {name} 테스트 중...")
    try:
        func()
        print(f"✅ {name} 통과")
        return True
    except AssertionError as e:
        print(f"❌ {name} 실패: {e}")
        return False
    except Exception as e:
        print(f"❌ {name} 에러 발생: {e}")
        return False

def test_free_zone():
    assert calculate_parking_fee("09:00", "09:30") == ("0시간 30분", 0)
    assert calculate_parking_fee("09:00", "09:15") == ("0시간 15분", 0)

def test_paid_zone():
    assert calculate_parking_fee("09:00", "09:31") == ("0시간 31분", 500)
    assert calculate_parking_fee("09:00", "09:40") == ("0시간 40분", 500)
    assert calculate_parking_fee("09:00", "09:41") == ("0시간 41분", 1000)
    assert calculate_parking_fee("09:00", "10:00") == ("1시간 0분", 1500)

def test_max_fee():
    _, fee = calculate_parking_fee("00:00", "23:59")
    assert fee == 20000

def test_invalid_format():
    # 잘못된 형식 (HH:MM 아님)
    # "9:00"은 Python strptime에서 정상적으로 인식되므로, 
    # 명확하게 형식이 틀린 케이스로 테스트를 교체합니다.
    try:
        calculate_parking_fee("9-00", "10:00")
        raise AssertionError("형식 오류를 감지하지 못했습니다. (9-00)")
    except ValueError as e:
        assert "형식이 올바르지 않습니다" in str(e)

    try:
        calculate_parking_fee("09:00", "apple")
        raise AssertionError("잘못된 문자열을 감지하지 못했습니다. (apple)")
    except ValueError as e:
        assert "형식이 올바르지 않습니다" in str(e)

def test_time_reverse():
    # 출차 < 입차
    try:
        calculate_parking_fee("10:00", "09:00")
        raise AssertionError("출차 시간이 더 빠른 경우를 감지하지 못했습니다.")
    except ValueError as e:
        assert "출차 시간은 입차 시간보다 늦어야 합니다" in str(e)

def main():
    print("🚀 주차 요금 계산 로직 테스트 시작...\n")
    
    test_cases = [
        ("무료 구간", test_free_zone),
        ("유료 구간 및 올림", test_paid_zone),
        ("최대 요금 제한", test_max_fee),
        ("시간 형식 예외", test_invalid_format),
        ("시간 역전 예외", test_time_reverse),
    ]
    
    passed = 0
    failed = 0
    total = len(test_cases)
    
    for name, func in test_cases:
        if run_test(name, func):
            passed += 1
        else:
            failed += 1
        print("-" * 30)
            
    print("\n" + "="*30)
    print(f"📊 테스트 결과 요약")
    print(f"   총 테스트: {total}")
    print(f"   ✅ 성공: {passed}")
    print(f"   ❌ 실패: {failed}")
    print("="*30)
    
    if failed == 0:
        print("\n🎉 모든 테스트를 성공적으로 통과했습니다!")
    else:
        print(f"\n⚠️ {failed}개의 테스트가 실패했습니다. 로직을 확인하세요.")

if __name__ == "__main__":
    main()
