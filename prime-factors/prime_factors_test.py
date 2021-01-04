import unittest

from prime_factors import factors

# Tests adapted from `problem-specifications//canonical-data.json`


class PrimeFactorsTest(unittest.TestCase):
    def test_no_factors(self):
        self.assertEqual(factors(1), [])

    def test_prime_number(self):
        self.assertEqual(factors(2), [2])

    def test_prime_number_2(self):
        self.assertEqual(factors(17), [17])

    def test_prime_number_3(self):
        self.assertEqual(factors(9539), [9539])

    def test_square_of_a_prime(self):
        self.assertEqual(factors(9), [3, 3])

    def test_square_of_a_prime_2(self):
        self.assertEqual(factors(625), [5, 5, 5, 5])

    def test_cube_of_a_non_prime(self):
        self.assertEqual(factors(27 ** 3), [3, 3, 3, 3, 3, 3, 3, 3, 3])

    def test_cube_of_a_prime(self):
        self.assertEqual(factors(617 ** 3), [617, 617, 617])

    def test_power_of_two(self):
        self.assertEqual(factors(1073741824), [2] * 30)

    def test_product_of_primes_and_non_primes(self):
        self.assertEqual(factors(48), [2, 2, 2, 2, 3])

    def test_product_of_primes(self):
        self.assertEqual(factors(901255), [5, 17, 23, 461])

    def test_factors_include_a_large_prime(self):
        self.assertEqual(factors(93819012551), [11, 9539, 894119])


if __name__ == "__main__":
    unittest.main()

#
# test_cube_of_a_prime (__main__.PrimeFactorsTest) ... ok
# test_factors_include_a_large_prime (__main__.PrimeFactorsTest) ... ok
# test_no_factors (__main__.PrimeFactorsTest) ... ok
# test_prime_number (__main__.PrimeFactorsTest) ... ok
# test_prime_number_2 (__main__.PrimeFactorsTest) ... ok
# test_prime_number_3 (__main__.PrimeFactorsTest) ... ok
# test_product_of_primes (__main__.PrimeFactorsTest) ... ok
# test_product_of_primes_and_non_primes (__main__.PrimeFactorsTest) ... ok
# test_square_of_a_prime (__main__.PrimeFactorsTest) ... ok
# test_square_of_a_prime_2 (__main__.PrimeFactorsTest) ... ok

# ----------------------------------------------------------------------
# Ran 10 tests in 1322.988s

# OK


## After introducing: incr.:
#
# test_cube_of_a_prime (__main__.PrimeFactorsTest) ... ok
# test_factors_include_a_large_prime (__main__.PrimeFactorsTest) ... ok
# test_no_factors (__main__.PrimeFactorsTest) ... ok
# test_prime_number (__main__.PrimeFactorsTest) ... ok
# test_prime_number_2 (__main__.PrimeFactorsTest) ... ok
# test_prime_number_3 (__main__.PrimeFactorsTest) ... ok
# test_product_of_primes (__main__.PrimeFactorsTest) ... ok
# test_product_of_primes_and_non_primes (__main__.PrimeFactorsTest) ... ok
# test_square_of_a_prime (__main__.PrimeFactorsTest) ... ok
# test_square_of_a_prime_2 (__main__.PrimeFactorsTest) ... ok

# ----------------------------------------------------------------------
# Ran 10 tests in 46.032s

# OK
