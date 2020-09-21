from __future__ import division
import unittest
import pytest

from rational_numbers import Rational

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class RationalNumbersTest(unittest.TestCase):

    # Tests of type: Arithmetic

    # Addition

    def test_add_two_positive_rational_numbers(self):
        self.assertEqual(Rational(1, 2) + Rational(2, 3), Rational(7, 6))

    def test_add_rational_number_and_integer(self):
        self.assertEqual(Rational(1, 2) + 2, Rational(5, 2))
        self.assertEqual(Rational(1, 2) + -2, Rational(-3, 2))
        self.assertEqual(Rational(1, 2) + 0, Rational(1, 2))

    def test_add_a_positive_rational_number_and_a_negative_rational_number(self):
        self.assertEqual(Rational(1, 2) + Rational(-2, 3), Rational(-1, 6))

    def test_add_two_negative_rational_numbers(self):
        self.assertEqual(Rational(-1, 2) + Rational(-2, 3), Rational(-7, 6))

    def test_add_a_rational_number_to_its_additive_inverse(self):
        self.assertEqual(Rational(1, 2) + Rational(-1, 2), Rational(0, 1))

    # Subtraction

    def test_subtract_two_positive_rational_numbers(self):
        self.assertEqual(Rational(1, 2) - Rational(2, 3), Rational(-1, 6))

    def test_subtract_integer_from_rational_number(self):
        self.assertEqual(Rational(1, 2) - 2, Rational(-3, 2))

    def test_subtract_a_positive_rational_number_and_a_negative_rational_number(self):
        self.assertEqual(Rational(1, 2) - Rational(-2, 3), Rational(7, 6))

    def test_subtract_two_negative_rational_numbers(self):
        self.assertEqual(Rational(-1, 2) - Rational(-2, 3), Rational(1, 6))

    def test_subtract_a_rational_number_from_itself(self):
        self.assertEqual(Rational(1, 2) - Rational(1, 2), Rational(0, 1))

    # Multiplication

    def test_multiply_two_positive_rational_numbers(self):
        self.assertEqual(Rational(1, 2) * Rational(2, 3), Rational(1, 3))

    def test_multiply_rational_numbers_by_integer(self):
        self.assertEqual(Rational(1, 2) * 2, Rational(1, 1))
        self.assertEqual(Rational(2, 7) * -3, Rational(-6, 7))

    def test_multiply_a_negative_rational_number_by_a_positive_rational_number(self):
        self.assertEqual(Rational(-1, 2) * Rational(2, 3), Rational(-1, 3))

    def test_multiply_two_negative_rational_numbers(self):
        self.assertEqual(Rational(-1, 2) * Rational(-2, 3), Rational(1, 3))

    def test_multiply_a_rational_number_by_its_reciprocal(self):
        self.assertEqual(Rational(1, 2) * Rational(2, 1), Rational(1, 1))

    def test_multiply_a_rational_number_by_1(self):
        self.assertEqual(Rational(1, 2) * Rational(1, 1), Rational(1, 2))

    def test_multiply_a_rational_number_by_0(self):
        self.assertEqual(Rational(1, 2) * Rational(0, 1), Rational(0, 1))

    # Division

    def test_divide_two_positive_rational_numbers(self):
        self.assertEqual(Rational(1, 2) / Rational(2, 3), Rational(3, 4))

    def test_divide_rational_number_by_integer(self):
        self.assertEqual(Rational(7, 4) / 2, Rational(7, 8))
        self.assertEqual(Rational(7, 4) / 3, Rational(7, 12))

    def test_divide_a_positive_rational_number_by_a_negative_rational_number(self):
        self.assertEqual(Rational(1, 2) / Rational(-2, 3), Rational(-3, 4))

    def test_divide_two_negative_rational_numbers(self):
        self.assertEqual(Rational(-1, 2) / Rational(-2, 3), Rational(3, 4))

    def test_divide_a_rational_number_by_1(self):
        self.assertEqual(Rational(1, 2) / Rational(1, 1), Rational(1, 2))

    # Tests of type: Absolute value

    def test_absolute_value_of_a_positive_rational_number(self):
        self.assertEqual(abs(Rational(1, 2)), Rational(1, 2))

    def test_absolute_value_of_a_positive_rational_number_with_negative_numerator_and_denominator(
        self
    ):
        self.assertEqual(abs(Rational(-1, -2)), Rational(1, 2))

    def test_absolute_value_of_a_negative_rational_number(self):
        self.assertEqual(abs(Rational(-1, 2)), Rational(1, 2))

    def test_absolute_value_of_a_negative_rational_number_with_negative_denominator(self):
        self.assertEqual(abs(Rational(1, -2)), Rational(1, 2))

    def test_absolute_value_of_zero(self):
        self.assertEqual(abs(Rational(0, 1)), Rational(0, 1))

    # Tests of type: Exponentiation of a rational number

    def test_raise_a_positive_rational_number_to_a_positive_integer_power(self):
        self.assertEqual(Rational(1, 2) ** 3, Rational(1, 8))

    def test_raise_a_negative_rational_number_to_a_positive_integer_power(self):
        self.assertEqual(Rational(-1, 2) ** 3, Rational(-1, 8))

    def test_raise_zero_to_an_integer_power(self):
        self.assertEqual(Rational(0, 1) ** 5, Rational(0, 1))

    def test_raise_one_to_an_integer_power(self):
        self.assertEqual(Rational(1, 1) ** 4, Rational(1, 1))

    def test_raise_a_positive_rational_number_to_the_power_of_zero(self):
        self.assertEqual(Rational(1, 2) ** 0, Rational(1, 1))

    def test_raise_a_positive_rational_number_to_the_negative_power(self):
        self.assertEqual(Rational(4, 5) ** -2, Rational(25, 16))

    def test_raise_a_negative_rational_number_to_the_power_of_zero(self):
        self.assertEqual(Rational(-1, 2) ** 0, Rational(1, 1))

    # Tests of type: Exponentiation of a real number to a rational number

    def test_raise_a_real_number_to_a_positive_rational_number(self):
        self.assertAlmostEqual(8 ** Rational(4, 3), 16.0, places=8)

    def test_raise_a_real_number_to_a_negative_rational_number(self):
        self.assertAlmostEqual(9 ** Rational(-1, 2), 0.3333333333333333, places=8)

    def test_raise_a_real_number_to_a_zero_rational_number(self):
        self.assertAlmostEqual(2 ** Rational(0, 1), 1.0, places=8)

    # Tests of type: Reduction to lowest terms

    def test_reduce_a_positive_rational_number_to_lowest_terms(self):
        self.assertEqual(Rational(2, 4), Rational(1, 2))

    def test_reduce_a_negative_rational_number_to_lowest_terms(self):
        self.assertEqual(Rational(-4, 6), Rational(-2, 3))

    def test_reduce_a_rational_number_with_a_negative_denominator_to_lowest_terms(self):
        self.assertEqual(Rational(3, -9), Rational(-1, 3))

    def test_reduce_zero_to_lowest_terms(self):
        self.assertEqual(Rational(0, 6), Rational(0, 1))

    def test_reduce_an_integer_to_lowest_terms(self):
        self.assertEqual(Rational(-14, 7), Rational(-2, 1))

    def test_reduce_one_to_lowest_terms(self):
        self.assertEqual(Rational(13, 13), Rational(1, 1))

    # Exceptions
    def test_rational_number_add_exception1(self):
        with pytest.raises(ValueError):
            Rational(1, 0)

    def test_rational_number_add_exception1(self):
        with pytest.raises(ValueError):
            self.assertEqual(Rational(1, 2) + 2.5)

    def test_rational_number_add_exception2(self):
        with pytest.raises(ValueError):
            self.assertEqual(Rational(1, 2) + None)

    def test_raise_rational_number_to_none(self):
        with pytest.raises(ValueError):
            self.assertEqual(Rational(1, 2) ** None)

    def test_raise_rational_number_to_float_power(self):
        with pytest.raises(ValueError):
            self.assertEqual(Rational(1, 2) ** 2.2)

    def test_raise_zero_to_a_zero_rational_number(self):
        with pytest.raises(ArithmeticError):
            0 ** Rational(0, 1)

    def test_raise_rational_0_to_a_zero_power(self):
        with pytest.raises(ArithmeticError):
            Rational(0, 1) ** 0

if __name__ == "__main__":
    unittest.main()
