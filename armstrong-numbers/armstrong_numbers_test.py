import unittest

from armstrong_numbers import is_armstrong_number

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class ArmstrongNumbersTest(unittest.TestCase):
    def test_zero_is_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(0), True)

    def test_single_digit_numbers_are_armstrong_numbers(self):
        self.assertIs(is_armstrong_number(5), True)

    def test_there_are_no_2_digit_armstrong_numbers(self):
        self.assertIs(is_armstrong_number(10), False)

    def test_three_digit_number_that_is_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(153), True)

    def test_three_digit_number_that_is_not_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(100), False)

    def test_four_digit_number_that_is_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(9474), True)

    def test_seven_digit_number_that_is_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(9926315), True)

    def test_seven_digit_number_that_is_not_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(9926314), False)

    def test_series_of_armstrong_number(self):
        for n in [1, 2, 3, 4, 6, 7, 8, 9, 370, 371, 407, 1634, 8208, 54748, 92727, 93084,
                  548834, 1741725, 4210818, 9800817, 24678050, 24678051, 88593477, 146511208,
                  472335975, 534494836, 912985153, 4679307774, 32164049650, 32164049651,
                  # BigInt, actually Int128
                  3706907995955475988644381, 19008174136254279995012734741,
                  186709961001538790100634132976991,
                  115132219018763992565095597973971522401]:
            self.assertIs(is_armstrong_number(n), True, f"Failed! n: {n} is an Armstrong Number!")

    def test_series_of_non_armstrong_number(self):
        for n in [9475, 9926314,
                  147808829414345923316083210206383297601001,
                  147808829414345923316083210206383297601]:
            self.assertIs(is_armstrong_number(n), False, f"Failed! n: {n} is NOT an Armstrong Number!")

if __name__ == "__main__":
    unittest.main()
