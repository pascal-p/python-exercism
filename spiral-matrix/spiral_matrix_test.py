import unittest

from spiral_matrix import spiral_matrix

# Tests adapted from `problem-specifications//canonical-data.json`


class SpiralMatrixTest(unittest.TestCase):
    def test_empty_spiral(self):
        self.assertEqual(spiral_matrix(0), [])

    def test_trivial_spiral(self):
        self.assertEqual(spiral_matrix(1), [[1]])

    def test_spiral_of_size_2(self):
        self.assertEqual(spiral_matrix(2), [[1, 2], [4, 3]])

    def test_spiral_of_size_3(self):
        self.assertEqual(spiral_matrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

    def test_spiral_of_size_4(self):
        self.assertEqual(
            spiral_matrix(4),
            [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]],
        )

    def test_spiral_of_size_5(self):
        self.assertEqual(
            spiral_matrix(5),
            [
                [1, 2, 3, 4, 5],
                [16, 17, 18, 19, 6],
                [15, 24, 25, 20, 7],
                [14, 23, 22, 21, 8],
                [13, 12, 11, 10, 9],
            ],
        )

    def test_spiral_of_size_6(self):
        self.assertEqual(
            spiral_matrix(6),
            [
                [1, 2, 3, 4, 5, 6],
                [20, 21, 22, 23, 24, 7],
                [19, 32, 33, 34, 25, 8],
                [18, 31, 36, 35, 26, 9],
                [17, 30, 29, 28, 27, 10],
                [16, 15, 14, 13, 12, 11]
            ],
        )

    def test_spiral_of_size_10(self):
        self.assertEqual(
            spiral_matrix(10),
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                [36, 37, 38, 39, 40, 41, 42, 43, 44, 11],
                [35, 64, 65, 66, 67, 68, 69, 70, 45, 12],
                [34, 63, 84, 85, 86, 87, 88, 71, 46, 13],
                [33, 62, 83, 96, 97, 98, 89, 72, 47, 14],
                [32, 61, 82, 95, 100, 99, 90, 73, 48, 15],
                [31, 60, 81, 94, 93, 92, 91, 74, 49, 16],
                [30, 59, 80, 79, 78, 77, 76, 75, 50, 17],
                [29, 58, 57, 56, 55, 54, 53, 52, 51, 18],
                [28, 27, 26, 25, 24, 23, 22, 21, 20, 19]
            ],
        )

if __name__ == "__main__":
    unittest.main()
