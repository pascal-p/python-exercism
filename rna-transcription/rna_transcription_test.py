import unittest

from rna_transcription import to_rna, to_rna_v1

LIST = [to_rna, to_rna_v1]

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.3.0

class RnaTranscriptionTest(unittest.TestCase):

    def test_empty_rna_sequence(self):
        _exp = ""
        for fn in LIST:
            self.assertEqual(to_rna(""), _exp,
                             f"{fn.__name__} should return {_exp} in this case")

    def test_rna_complement_of_cytosine_is_guanine(self):
        _exp = "G"
        for fn in LIST:
            self.assertEqual(to_rna("C"), _exp,
                             f"{fn.__name__} should return {_exp} in this case")

    def test_rna_complement_of_guanine_is_cytosine(self):
        _exp = "C"
        for fn in LIST:
            self.assertEqual(to_rna("G"), _exp,
                             f"{fn.__name__} should return {_exp} in this case")

    def test_rna_complement_of_thymine_is_adenine(self):
        _exp = "A"
        for fn in LIST:
            self.assertEqual(to_rna("T"), _exp,
                             f"{fn.__name__} should return {_exp} in this case")

    def test_rna_complement_of_adenine_is_uracil(self):
        _exp = "U"
        for fn in LIST:
            self.assertEqual(to_rna("A"), _exp,
                             f"{fn.__name__} should return {_exp} in this case")

    def test_rna_complement(self):
        _exp = "UGCACCAGAAUU"
        for fn in LIST:
            self.assertEqual(to_rna("ACGTGGTCTTAA"), _exp,
                             f"{fn.__name__} should return {_exp} in this case")

    def test_non_valid_strand1(self):
        "not valid here: means contains something else than A, C, G, T - case matters"
        for fn in LIST:
            with self.assertRaisesWithMessage(ValueError,
                                              f"{fn.__name__} should raise exception"):
                fn("ACFEAHJDKHAKDHS")

    def test_non_valid_strand_lowercase(self):
        "not valid here: means contains something else than A, C, G, T - case matters"
        for fn in LIST:
            with self.assertRaisesWithMessage(ValueError,
                                              f"{fn.__name__} should raise exception"):
                fn("acgt")

    def test_non_valid_strand_extra_chars(self):
        "not valid here: means contains something else than A, C, G, T - case matters"
        for fn in LIST:
            with self.assertRaisesWithMessage(ValueError,
                                              f"{fn.__name__} should raise exception"):
                fn("A C. G. T")



    # Utility functions
    def assertRaisesWithMessage(self, exception, msg=None):
        return self.assertRaisesRegex(exception, r".+", msg=msg)

if __name__ == "__main__":
    unittest.main()
