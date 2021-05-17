import unittest

from nth_prime import prime

# Tests adapted from `problem-specifications//canonical-data.json`


def prime_range(n):
    """Returns a list of the first n primes"""
    return [prime(i) for i in range(1, n + 1)]


class NthPrimeTest(unittest.TestCase):
    def test_first_prime(self):
        self.assertEqual(prime(1), 2)

    def test_second_prime(self):
        self.assertEqual(prime(2), 3)

    def test_sixth_prime(self):
        self.assertEqual(prime(6), 13)

    def test_16th_prime(self):
        self.assertEqual(prime(16), 53)

    def test_1049th_prime(self):
        self.assertEqual(prime(1049), 8377)

    def test_big_prime(self):
        self.assertEqual(prime(10001), 104743)

    def test_bigger_prime(self):
        self.assertEqual(prime(100_001, lim=10_000_000), 1299721)

    def test_there_is_no_zeroth_prime(self):
        with self.assertRaisesWithMessage(ValueError):
            prime(0)

    # Additional tests for this track
    def test_first_twenty_primes(self):
        self.assertEqual(
            prime_range(20),
            [
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
            ],
        )

    def test_first_hundred_primes(self):
        self.assertEqual(
            prime_range(100),
            [
                2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
                127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
                179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
                233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
                283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
                353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
                419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
                467, 479, 487, 491, 499, 503, 509, 521, 523, 541
            ],
        )


    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
