import unittest
from logic import convert

class TestUnitConverter(unittest.TestCase):
    
    # 1. 숫자 유효성 검사 테스트
    def test_non_numeric_input(self):
        result, notice = convert("abc", "cm", "m")
        self.assertEqual(result, "")
        self.assertEqual(notice, "숫자를 입력해주세요")

    def test_empty_input(self):
        result, notice = convert("", "cm", "m")
        self.assertEqual(result, "")
        self.assertEqual(notice, "숫자를 입력해주세요")

    # 2. 단위 호환성 검사 테스트
    def test_mismatched_units_length_and_temp(self):
        result, notice = convert("10", "m", "°C")
        self.assertEqual(result, "")
        self.assertEqual(notice, "길이와 온도는 변환할 수 없습니다")

    def test_mismatched_units_temp_and_length(self):
        result, notice = convert("32", "°F", "cm")
        self.assertEqual(result, "")
        self.assertEqual(notice, "길이와 온도는 변환할 수 없습니다")

    # 3. 정상 변환 케이스 테스트 (길이)
    def test_length_conversion_m_to_cm(self):
        result, notice = convert("1", "m", "cm")
        self.assertEqual(result, "100.0")
        self.assertEqual(notice, "")

    def test_length_conversion_km_to_mm(self):
        result, notice = convert("1", "km", "mm")
        self.assertEqual(result, "1000000.0")
        self.assertEqual(notice, "")

    def test_length_conversion_cm_to_m(self):
        result, notice = convert("150", "cm", "m")
        self.assertEqual(result, "1.5")
        self.assertEqual(notice, "")

    # 4. 정상 변환 케이스 테스트 (온도)
    def test_temp_conversion_c_to_f(self):
        result, notice = convert("0", "°C", "°F")
        self.assertAlmostEqual(float(result), 32.0)
        self.assertEqual(notice, "")

    def test_temp_conversion_f_to_c(self):
        result, notice = convert("212", "°F", "°C")
        self.assertAlmostEqual(float(result), 100.0)
        self.assertEqual(notice, "")

if __name__ == "__main__":
    unittest.main()

