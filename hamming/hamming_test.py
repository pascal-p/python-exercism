import unittest

from hamming import distance, distance_v1, distance_v2

# Tests adapted from `problem-specifications//canonical-data.json` @ v2.3.0
LIST = [distance, distance_v1, distance_v2]

class HammingTest(unittest.TestCase):
    def test_empty_strands(self):
        _exp = 0
        for fn in LIST:
            self.assertEqual(fn("", ""), _exp,
                             f"{fn.__name__} should return {_exp} in this case")

    def test_single_letter_identical_strands(self):
        _exp = 0
        for fn in LIST:
            self.assertEqual(fn("A", "A"), _exp,
                             f"{fn.__name__} should return {_exp} in this case")

    def test_single_letter_different_strands(self):
        _exp = 1
        for fn in LIST:
            self.assertEqual(fn("G", "T"), _exp,
                             f"{fn.__name__} should return {_exp} in this case")

    def test_long_identical_strands(self):
        _exp = 0
        for fn in LIST:
            self.assertEqual(fn("GGACTGAAATCTG", "GGACTGAAATCTG"), _exp,
                             f"{fn.__name__} should return {_exp} in this case")

    def test_long_different_strands(self):
        _exp = 9
        for fn in LIST:
            self.assertEqual(fn("GGACGGATTCTG", "AGGACGGATTCT"), _exp,
                             f"{fn.__name__} should return {_exp} in this case")

    def test_long_different_strands(self):
        _exp = 94
        for fn in LIST:
            self.assertEqual(fn("ATACCTACCGGTACGGGTTTACACATGAGGTTGTTGCCCTTTCAATCTTTCAAGCTTCCTCCGGGCAATTCATCCGAGTTCGTGACGATACTCCGGAATTTAAGGCCCTCTTCCGTTCGTGAGGCAGA",
                                "TCCGTCAAGAATCCACCAGCCAACATCCTGCCTCCAGTAGTAAAAGCTAGTCCATGGCTGAGGGAACTCGGTTATAGGAACGATCAACTACGTGTCCGCGTTCCGATCCGCACTGTCCGATAATGACA"), _exp,
                             f"{fn.__name__} should return {_exp} in this case")

    def test_very_long_diff_strands(self):
        _exp = 742
        for fn in LIST:
            self.assertEqual(fn("GTTCCAGGAGTTGAAGTTCGTCACCAGTCGAAGTTCCGCGTTTATATTCTCCCGTAAACGAACCAAGATGTGTTGCACGACCCCATACCGGGTCCACTCATACCCCACAGCAAGGGTTCTACAGTCCATGAGCACACAGCCCCAAGTCAGTTTCAATTCCACACTGAGATTAAGTAACTCTATTACTGCGCTGTTCAACATCGCAGAGGCACCAAAATCTCAACTGTCGGGCAGGACAGGATCCACATACTACTGAGTCCTATCAGACCTTGTTCTAACCCCGATGTGCCAAACCTTCTGGGACTGAATTCATCTGCTGCAAGTTTAGGAGGCGATTAGGACAACCGATCTCCCCGAAGGATTCTAGCTCTATGATCGGCTTTGATCCCCAAGAGGCTCAGGTGCTTAATGGACATGCGGGGTATAACGTCGAAGATTATGATTATCGTTAAGTTGTGCGCTTGCCTGTTCACGGACGACGCTCACGCGTCTCTCAGGCTTCCTTCATCGCCGGGAGGACGGGCCGTGTTACATGGCTAAGGTCTATTACTTATGTCGAAGATTCATGTTTTTAGTAGCGTGAACCTGGAGACTCATGGACTCGAAACCAATATCATACGTCAAGGTTCTAGGCCGTCACCTGGTGCTGATGTGAATAGCCATACGGCAAACGCAGTACCGTTTCCACTCAGCAGACTTGACGAAAGAGCTCCTCCAGATGGTCTCTGTTCGTAGCACGTTGGCGGTTAAGGAGTCCGAGGTTGTAGATCGTATACTAATTCGGCATTTCATAGGGTCCCCGATCTTAAGCAGTCTAACCCACACGTGGTTCCTTGGAGGTACCCTTAGTTCCGTCCAGCTGGCACGGCTGCTAGCATCGATAGCATGTGTCCCTTTAGGTTCTGAGCGAGTCCGCGTCGCTCAAGTTTTACGGCGACTCCTTACGTTGAATACGCCTCGCACTAACTCAGGACCGGGAAGATAACGATGCGGATTTTGGGATGTCTTCGCGAGGGGGCTACGG",
                                "CATAATCATCCTTGATGTTCTTTGCCTCGACGGAAGACTAAAGTTTCGTCGCCCACAATTAAGATGCTGATGGCTGGACCAACCATAGCTTAACGCCTAGGATTGCTTTGCTGTCACCAACTTCCGCGGGTGATCTGGCCAAGCTATCACAGTTGATTGTCTTCGTGCCAATTATAAAAAACTCGCTATGAATGCAATTGGCTCCTCTGGGCGTCGACCTTTTGCTCGATAGGGCGGTTAGTATTCAGGTCCTCGCTTCCTCTACCAGCACACGGGCTACGCCGGCTGCATATCATCGGGTCAGGGTATTTGTCGCCTCTCTGGCGCAGAATGTCATACATACGTCTACGACTGACTCGGCCGGTCGCATTGTTTACGGACCCGACGTCCAAGTACGATAACCCCACGCGCGTACGCCAGCAACTATTGATCCAGCTTTATTAAGGTAGGTGGGCGCATTCGCACCCCTCTTAGTAATACCATCTAGAGGACCTCGGATGGGTCTTCCTGTACTTAATTACTTTAATCGATACCTTATTTCGCTAACGACTCGTTGAATTCGTTTTCACCGTCGGCCGTGGACTTCTCGTTACGCCCTTACCCTTTGTGTAGACGATTCCCAGCCATGGACCATCAGTATAGGGCGTGCTGCAGCCTTAGCAGCTATTATGGCGCCTCCGGTAGCAAGATAGAACTATTGCACAAAGAACGGCTATACGCCGAACCATGATTCTTGTGACCAAACCTACAAGGGCGCCTAAGAGCAAACTAGGATTGTGGTTTTTTAGTCGTAAAAGGCTAGCTTCTCGGATTTTACTTTCTCTACGTAACCGTTCGTCCCCTTTCGTATCTTCAAAGTTAGCCAACTGCGCGAGTAGTTAAACTCGCCGGGGCTATTGCAAATGAAGTAATCTTGTATATAGTTCAGAGCTAGTTAATGGTAGTCAGTGGCCGAAGTTTTCGCCTCAGACGAGAATACTAGCACCGATATAAATAGGGGCCTTGATACTTGGAGTGGCGAGCG"), _exp,
                             f"{fn.__name__} should return {_exp} in this case")

    def test_disallow_first_strand_longer(self):
        for fn in LIST:
            with self.assertRaisesWithMessage(ValueError,
                                              f"{fn.__name__} should raise exception"):
                fn("AATG", "AAA")

    def test_disallow_second_strand_longer(self):
        for fn in LIST:
            with self.assertRaisesWithMessage(ValueError,
                                              f"{fn.__name__} should raise exception"):
                fn("ATA", "AGTG")

    def test_disallow_left_empty_strand(self):
        for fn in LIST:
            with self.assertRaisesWithMessage(ValueError,
                                              f"{fn.__name__} should raise exception"):
                fn("", "G")

    def test_disallow_right_empty_strand(self):
        for fn in LIST:
            with self.assertRaisesWithMessage(ValueError,
                                              f"{fn.__name__} should raise exception"):
                fn("G", "")

    # Utility functions
    def assertRaisesWithMessage(self, exception, msg=None):
        return self.assertRaisesRegex(exception, r".+", msg=msg)


if __name__ == "__main__":
    unittest.main()
