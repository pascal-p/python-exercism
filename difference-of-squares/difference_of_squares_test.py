import unittest

from difference_of_squares import difference_of_squares, square_of_sum, sum_of_squares

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0


class DifferenceOfSquaresTest(unittest.TestCase):
    def test_square_of_sum_1(self):
        self.assertEqual(square_of_sum(1), 1)

    def test_square_of_sum_5(self):
        self.assertEqual(square_of_sum(5), 225)

    def test_square_of_sum_100(self):
        self.assertEqual(square_of_sum(100), 25502500)

    def test_sum_of_squares_1(self):
        self.assertEqual(sum_of_squares(1), 1)

    def test_sum_of_squares_5(self):
        self.assertEqual(sum_of_squares(5), 55)

    def test_sum_of_squares_100(self):
        self.assertEqual(sum_of_squares(100), 338350)

    def test_difference_of_squares_1(self):
        self.assertEqual(difference_of_squares(1), 0)

    def test_difference_of_squares_5(self):
        self.assertEqual(difference_of_squares(5), 170)

    def test_difference_of_squares_100(self):
        self.assertEqual(difference_of_squares(100), 25164150)

    def test_difference_of_squares_with_large_val(self):
        for n, exp in [
                (5_000, 156270827082500),
                (4_000_000, 64000010666662666666000000),
                (900_000_000_000_000_000_000,
                 164_025_000_000_000_000_000_121_499_999_999_999_999_999_797_499_999_999_999_999_999_850_000_000_000_000_000_000)
        ]:
            self.assertEqual(difference_of_squares(n), exp)


if __name__ == "__main__":
    unittest.main()
