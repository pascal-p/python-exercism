import unittest

from collatz_conjecture import steps

# Tests adapted from `problem-specifications//canonical-data.json`


class CollatzConjectureTest(unittest.TestCase):
    def test_zero_steps_for_one(self):
        self.assertEqual(steps(1), 0)

    def test_divide_if_even(self):
        self.assertEqual(steps(16), 4)

    def test_even_and_odd_steps(self):
        self.assertEqual(steps(12), 9)

    def test_large_number_of_even_and_odd_steps(self):
        self.assertEqual(steps(1000000), 152)

    def test_load(self):
        for n, exp in [
                (19, 20), (27, 111), (97, 118), (871, 178),
                (6171, 261), (77031, 350), (837_799, 524),
                (8_400_511, 685), (63_728_127, 949), (670_617_279, 986),
                (9_780_657_630, 1132), (75_128_138_247, 1228),
                (989_345_275_647, 1348),
                (7_887_663_552_367, 1563),
                (80_867_137_596_217, 1662),
                (134_345_724_286_089, 1823),
                (530_149_921_398_649, 1856),
                (942_488_749_153_153, 1862),
                (1_675_535_554_050_049, 1868),
                (3_586_720_916_237_671, 1895),
                (4_320_515_538_764_287, 1903),
                (4_861_718_551_722_727, 1916),
                (12_769_884_180_266_527, 2039),
                (17_026_512_240_355_369, 2042),
                (7_579_309_213_675_935, 1958),
                (93_571_393_692_802_302, 2091),
                (372_975_273_994_315_489, 2261),
                (931_386_509_544_713_451, 2283),
                (1_339_302_163_616_345_727, 2330),
                (1_278_775_404_785_934_855, 2286),
        ]:
            self.assertEqual(steps(n), exp) 

    def test_zero_is_an_error(self):
        with self.assertRaisesWithMessage(ValueError):
            steps(0)

    def test_negative_value_is_an_error(self):
        with self.assertRaisesWithMessage(ValueError):
            steps(-15)
            
    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
