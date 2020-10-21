import unittest

from rail_fence_cipher import decode, encode

# Tests adapted from `problem-specifications//canonical-data.json`


class RailFenceCipherTest(unittest.TestCase):
    def test_encode_with_two_rails(self):
        self.assertMultiLineEqual(encode("XOXOXOXOXOXOXOXOXO", 2), "XXXXXXXXXOOOOOOOOO")
        self.assertMultiLineEqual(encode("FOOBARS", 2), "FOASOBR")
        self.assertMultiLineEqual(encode("FOO BAR S!", 2), "FOASOBR")

    def test_encode_with_three_rails(self):
        self.assertMultiLineEqual(
            encode("WEAREDISCOVEREDFLEEATONCE", 3), "WECRLTEERDSOEEFEAOCAIVDEN"
        )
        self.assertMultiLineEqual(
            encode("we are discovered, flee at once!", 3), "WECRLTEERDSOEEFEAOCAIVDEN"
        )
        self.assertMultiLineEqual(encode("FOOBARS", 3), "FAOBROS")

    def test_encode_with_ending_in_the_middle(self):
        self.assertMultiLineEqual(encode("EXERCISES", 4), "ESXIEECSR")

    def test_encode_with_five_rails(self):
        self.assertMultiLineEqual(encode("FOOBARS", 5), "FOOSBRA")
        self.assertMultiLineEqual(encode("The Devil Is In The Details.", 5), "TIEHLSDTEIIEADVNHISETL")

    def test_encode_with_six_rails(self):
        self.assertMultiLineEqual(encode("FOOBARS", 6), "FOOBASR")

    def test_decode_with_three_rails(self):
        self.assertMultiLineEqual(
            decode("TEITELHDVLSNHDTISEIIEA", 3), "THEDEVILISINTHEDETAILS"
        )

    def test_decode_with_five_rails(self):
        self.assertMultiLineEqual(decode("EIEXMSMESAORIWSCE", 5), "EXERCISMISAWESOME")

    def test_decode_with_six_rails(self):
        self.assertMultiLineEqual(
            decode("133714114238148966225439541018335470986172518171757571896261", 6),
            "112358132134558914423337761098715972584418167651094617711286",
        )

    def test_encode_deocde_identity(self):
        for msg, rails in [
                ("XOXOXOXOXOXOXOXOXO", 2),
                ("WEAREDISCOVEREDFLEEATONCE", 3),
                ("THEDEVILISINTHEDETAILS", 3),
                ("THEDEVILISINTHEDETAILS", 5),
                ("133714114238148966225439541018335470986172518171757571896261", 6)
        ]:
            self.assertMultiLineEqual(decode(encode(msg, rails), rails), msg)


if __name__ == "__main__":
    unittest.main()
