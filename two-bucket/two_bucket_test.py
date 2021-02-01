import unittest

from two_bucket import measure

# Tests adapted from `problem-specifications//canonical-data.json`


class TwoBucketTest(unittest.TestCase):
    def test_measure_using_b1_of_size_3_and_b2_of_size_5_start_with_b1_1(
        self
    ):
        self.assertEqual(measure(3, 5, 1, "one"), (4, "one", 5))

    def test_measure_using_b1_of_size_5_and_b2_of_size_3_start_with_b1_2_4(
        self
    ):
        # make 4L
        self.assertEqual(measure(5, 3, 4, "one"), (6, "one", 3))
        self.assertEqual(measure(5, 3, 4, "two"), (8, "one", 0))

    def test_measure_using_b1_of_size_5_and_b2_of_size_3_start_with_b1_2_7(
        self
    ):
        # make 7L
        self.assertEqual(measure(5, 3, 7, "one"), (6, "two", 4))
        self.assertEqual(measure(5, 3, 7, "two"), (10, "two", 5))

    def test_measure_using_b1_of_size_3_and_b2_of_size_5_start_with_b2_1(
        self
    ):
        self.assertEqual(measure(3, 5, 1, "two"), (8, "two", 3))

    def test_measure_using_b1_of_size_5_and_b2_of_size_3_start_with_b2_4(
        self
    ):
        # make 4L
        self.assertEqual(measure(5, 3, 4, "two"), (8, "one", 0))

    def test_measure_using_b1_of_size_7_and_b2_of_size_11_start_with_b1(
        self
    ):
        self.assertEqual(measure(7, 11, 2, "one"), (14, "one", 11))

    def test_measure_using_b1_of_size_7_and_b2_of_size_11_start_with_b2(
        self
    ):
        self.assertEqual(measure(7, 11, 2, "two"), (18, "two", 7))

    def test_measure1_step_using_b1_of_size_1_and_b2_of_size_3_start_with_b2(
        self
    ):
        self.assertEqual(measure(1, 3, 3, "two"), (1, "two", 0))


    def test_measure_using_b1_of_size_6_and_b2_of_size_15_start_with_b1_4_impossible(
        self
    ):
        with self.assertRaisesWithMessage(ValueError):
            self.assertEqual(measure(6, 15, 4, "one"))

    def test_measure_using_b1_of_size_6_and_b2_of_size_15_start_with_b1_1_2(
        self
    ):
        self.assertEqual(measure(6, 15, 9, "one"), (10, "two", 0))
        self.assertEqual(measure(6, 15, 9, "two"), (2, "two", 6))


    # def test_measure_using_b1_of_size_2_and_b2_of_size_3_start_with_b1_and_end_with_b2(
    #    self
    #):
    #    self.assertEqual(measure(2, 3, 3, "one"), (2, "two", 2))

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
