import unittest

from diffie_hellman import private_key, public_key, secret, \
    s_private_key, s_public_key, s_secret

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0


class DiffieHellmanTest(unittest.TestCase):
    def test_private_key_is_in_range_1_p(self):
        primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for p in primes:
            self.assertTrue(1 < private_key(p) < p)

    def test_exception_not_prime(self):
        with self.assertRaises(ValueError):
            private_key(65536)

    def test_exception_not_in_range1(self):
        with self.assertRaises(ValueError):
            private_key(-1)

    def test_exception_not_in_range2(self):
        with self.assertRaises(ValueError):
            private_key(0)

    def test_private_key_is_random(self):
        """
        Can fail due to randomness, but most likely will not,
        due to pseudo-randomness and the large number chosen
        """
        p = 2147483647
        private_keys = [private_key(p) for _ in range(5)]
        self.assertEqual(len(set(private_keys)), len(private_keys))

    def test_can_calculate_public_key_using_private_key(self):
        p = 23
        g = 5
        private_key = 6
        self.assertEqual(8, public_key(p, g, private_key))

    def test_can_calculate_secret_using_other_party_s_public_key(self):
        p = 23
        their_public_key = 19
        my_private_key = 6
        self.assertEqual(2, secret(p, their_public_key, my_private_key))

    def test_key_exchange(self):
        p = 23
        g = 5
        alice_private_key = private_key(p)
        bob_private_key = private_key(p)
        alice_public_key = public_key(p, g, alice_private_key)
        bob_public_key = public_key(p, g, bob_private_key)
        secret_a = secret(p, bob_public_key, alice_private_key)
        secret_b = secret(p, alice_public_key, bob_private_key)
        self.assertTrue(secret_a == secret_b)

    #
    def test_private_key_is_in_range_1_p(self):
        primes = [100000937, 100000939,100000963,100000969,100001029,100001053,100001059,100001081,100001087,100001107,
                  100001119,100001131,100001147,100001159,100001177,100001183,100001203,100001207,100001219,100001227]
        for p in primes:
            self.assertTrue(1 < s_private_key(p) < p)

    def test_private_key_is_random(self):
        """
        Can fail due to randomness, but most likely will not,
        due to pseudo-randomness and the large number chosen
        """
        p = 527892224099
        private_keys = [s_private_key(p) for _ in range(5)]
        self.assertEqual(len(set(private_keys)), len(private_keys))

    def test_can_calculate_public_key_using_private_key(self):
        p = 29501
        g = 8713
        private_key = 29331
        self.assertEqual(15518, s_public_key(p, g, private_key))

    def test_can_calculate_secret_using_other_party_s_public_key(self):
        p = 29501
        their_public_key = 8017
        my_private_key = 8849
        self.assertEqual(184, s_secret(p, their_public_key, my_private_key))

    def test_key_exchange(self):
        p = 29501
        g = 2147483647
        alice_private_key = s_private_key(p)
        bob_private_key = s_private_key(p)
        alice_public_key = s_public_key(p, g, alice_private_key)
        bob_public_key = s_public_key(p, g, bob_private_key)
        secret_a = s_secret(p, bob_public_key, alice_private_key)
        secret_b = s_secret(p, alice_public_key, bob_private_key)
        self.assertTrue(secret_a == secret_b)



if __name__ == "__main__":
    unittest.main()
