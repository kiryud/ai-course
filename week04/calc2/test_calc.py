from calc import Calculator

def test_calculator():
    calc = Calculator()
    
    test_cases = [
        ([], "0"),
        (["1", "2", "+", "3", "="], "15"),
        (["2", "+", "3", "*", "4", "="], "20"),
        (["5", "+", "-", "3", "="], "2"),
        (["0", ".", "1", "+", "0", ".", "2", "="], "0.3"),
        (["6", "/", "3", "="], "2"),
        (["7", "/", "2", "="], "3.5"),
        (["5", "/", "0", "="], "0으로 나눌 수 없습니다"),
        (["5", "/", "0", "=", "7"], "0으로 나눌 수 없습니다"),
        (["5", "/", "0", "=", "C"], "0"),
        (["1", ".", ".", "5"], "1.5"),
        ([".", ], "0."),
        (["0", "0", "7"], "7"),
        (["1", "2", "3", "BS"], "12"),
        (["5", "BS"], "0"),
        (["9", "+/-"], "-9"),
        (["5", "0", "%"], "0.5"),
        (["2", "+", "3", "=", "4"], "4"),
        (["2", "+", "3", "=", "+", "4", "="], "9"),
        (["2", "+", "3", "=", "=", "5"], "5"),
    ]

    passed = 0
    for i, (inputs, expected) in enumerate(test_cases):
        calc._reset()
        for key in inputs:
            calc.press(key)
        
        actual = calc.display
        if actual == expected:
            passed += 1
        else:
            print(f"Test {i+1} failed: input={inputs}, expected={expected}, actual={actual}")

    if passed == len(test_cases):
        print(f"모든 테스트 통과 ({passed}개)")
    else:
        print(f"테스트 실패: {len(test_cases) - passed}개 실패")

if __name__ == "__main__":
    test_calculator()
