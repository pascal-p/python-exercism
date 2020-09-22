import unittest
import pytest

from roman_numerals import roman

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0
class RomanNumeralsTest(unittest.TestCase):
    def test_1_is_a_single_i(self):
        self.assertEqual(roman(1), "I")

    def test_2_is_two_i_s(self):
        self.assertEqual(roman(2), "II")

    def test_3_is_three_i_s(self):
        self.assertEqual(roman(3), "III")

    def test_4_being_5_1_is_iv(self):
        self.assertEqual(roman(4), "IV")

    def test_5_is_a_single_v(self):
        self.assertEqual(roman(5), "V")

    def test_6_being_5_1_is_vi(self):
        self.assertEqual(roman(6), "VI")

    def test_9_being_10_1_is_ix(self):
        self.assertEqual(roman(9), "IX")

    def test_20_is_two_x_s(self):
        self.assertEqual(roman(27), "XXVII")

    def test_48_is_not_50_2_but_rather_40_8(self):
        self.assertEqual(roman(48), "XLVIII")

    def test_49_is_not_40_5_4_but_rather_50_10_10_1(self):
        self.assertEqual(roman(49), "XLIX")

    def test_50_is_a_single_l(self):
        self.assertEqual(roman(59), "LIX")

    def test_90_being_100_10_is_xc(self):
        self.assertEqual(roman(93), "XCIII")

    def test_100_is_a_single_c(self):
        self.assertEqual(roman(141), "CXLI")

    def test_60_being_50_10_is_lx(self):
        self.assertEqual(roman(163), "CLXIII")

    def test_400_being_500_100_is_cd(self):
        self.assertEqual(roman(402), "CDII")

    def test_500_is_a_single_d(self):
        self.assertEqual(roman(575), "DLXXV")

    def test_900_being_1000_100_is_cm(self):
        self.assertEqual(roman(911), "CMXI")

    def test_1000_is_a_single_m(self):
        self.assertEqual(roman(1024), "MXXIV")

    def test_1703_is_a_single_m(self):
        self.assertEqual(roman(1703), "MDCCIII")

    def test_1991_is_a_two_m(self):
        self.assertEqual(roman(1991), "MCMXCI")

    def test_3000_is_three_m_s(self):
        self.assertEqual(roman(3000), "MMM")

    def test_convert_10_to_20(self):
        spec = [(100, "C"), (200, "CC"), (300, "CCC"), (400, "CD"), (500, "D"),
                (600, "DC"), (700, "DCC"), (800, "DCCC"), (900, "CM")]
        for (num, exp) in spec:
            self.assertEqual(roman(num), exp)

    def test_convert_1xx(self):
        spec = [(100, "C"), (200, "CC"), (300, "CCC"), (400, "CD"), (500, "D"),
                (600, "DC"), (700, "DCC"), (800, "DCCC"), (900, "CM")]
        for (num, exp) in spec:
            self.assertEqual(roman(num), exp)

    # Exceptions
    def test_exception_roman_0_not_defined(self):
        with pytest.raises(ValueError):
            roman(0)

    def test_exception_roman_negative_not_defined(self):
        with pytest.raises(ValueError):
            roman(-11)

    def test_exception_over_3000(self):
        with pytest.raises(ValueError):
            roman(3001)

    def test_exception_convert_a_float(self):
        with pytest.raises(TypeError):
            roman(3.11)

    def test_exception_convert_a_string(self):
        with pytest.raises(TypeError):
            roman('FOOBAR')

if __name__ == "__main__":
    unittest.main()
