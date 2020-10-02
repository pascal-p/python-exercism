import unittest

from affine_cipher import decode, encode

# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0

LongStr =  """
Chor. Two households, both alike in dignity,
In fair Verona, where we lay our scene,
From ancient grudge break to new mutiny,
Where civil blood makes civil hands unclean.
From forth the fatal loins of these two foes
A pair of star-cross'd lovers take their life;
Whose misadventur'd piteous overthrows
Doth with their death bury their parents' strife,
The fearful passage of their death-mark'd love,
And the continuance of their parents' rage,
 Which, but their children's end, naught could remove,
Is now the two hours' traffic of our stage;
The which if you with patient ears attend,
What here shall miss, our toil shall strive to mend.
"""

class AffineCipherTest(unittest.TestCase):

    ## Encode
    def test_encode_yes(self):
        self.assertEqual(encode("yes", 5, 7), "xbt")

    def test_encode_test(self):
        self.assertEqual(encode("Test", 5, 7), "ybty")

    def test_encode_no(self):
        self.assertEqual(encode("no", 15, 18), "fu")

    def test_encode_omg(self):
        self.assertEqual(encode("OMG", 21, 3), "lvz")

    def test_encode_o_m_g(self):
        self.assertEqual(encode("O M G", 25, 47), "hjp")

    def test_encode_mindblowingly(self):
        self.assertEqual(encode("mindblowingly", 11, 15), "rzcwa gnxzc dgt")

    def test_encode_numbers(self):
        self.assertEqual(
            encode("Testing,1 2 3, testing.", 3, 4), "jqgjc rw123 jqgjc rw"
        )

    def test_encode_deep_thought(self):
        self.assertEqual(encode("Truth is fiction.", 5, 17), "iynia fdqfb ifje")

    def test_encode_deep_thought_nospc(self):
        self.assertEqual(encode("Truthisfiction.", 5, 17), "iynia fdqfb ifje")

    def test_encode_thought(self):
        self.assertEqual(encode("Free Will is a delusion. Face it", 7, 17),
                         "agttp vqqvn rmtqb nvlea rftvu")

    def test_encode_all_the_letters(self):
        self.assertEqual(
            encode("The quick brown fox jumps over the lazy dog.", 17, 33),
            "swxtj npvyk lruol iejdc blaxk swxmh qzglf",
        )

    def test_encode_with_no_spaces_in_input2(self):
        self.assertEqual(
            encode("tgxknetbyjznxaejgtnejoozgrnexgj", 23, 31),
            "anobs tacle isoft enast eppin gston e",
        )

    def test_encode_lon_str(self):
        self.assertEqual(
            encode(LongStr, 17, 19),
            """bixwe dxixv njixy snkxe ityzh jzgsz rgzel zgatz wmjwx gtdij wjdjy tlxvw nbjgj awxpt gbzjg erwvs rjkwj thexg jdpve zgldi jwjbz mzyky xxspt hjnbz mzyit gsnvg byjtg awxpa xweie ijate tyyxz gnxae ijnje dxaxj ntotz wxane twbwx nnsyx mjwne thjei jzwyz ajdix njpzn tsmjg evwso zejxv nxmjw eiwxd nsxei dzeie ijzws jteik vwlei jzwot wjgen newza jeija jtwav yotnn trjxa eijzw sjtei ptwhs yxmjt gseij bxgez gvtgb jxaei jzwot wjgen wtrjd izbik veeij zwbiz yswjg njgsg tvrie bxvys wjpxm jzngx deije dxixv wnewt aazbx axvwn etrje ijdiz bizal xvdze iotez jgejt wntee jgsdi teijw jnity ypznn xvwex zynit yynew zmjex pjgs"""
        )

    def test_encode_with_a_not_coprime_to_m(self):
        with self.assertRaisesWithMessage(ValueError):
            encode("This is a test.", 6, 17)


    ## Decode
    def test_decode_exercism(self):
        self.assertEqual(decode("tytgn fjr", 3, 7), "exercism")

    def test_decode_test(self):
        self.assertEqual(decode("ybty", 5, 7), "test")

    def test_decode_a_sentence(self):
        self.assertEqual(
            decode("qdwju nqcro muwhn odqun oppmd aunwd o", 19, 16),
            "anobstacleisoftenasteppingstone",
        )

    def test_decode_numbers(self):
        self.assertEqual(decode("odpoz ub123 odpoz ub", 25, 7), "testing123testing")

    def test_decode_all_the_letters(self):
        self.assertEqual(
            decode("swxtj npvyk lruol iejdc blaxk swxmh qzglf", 17, 33),
            "thequickbrownfoxjumpsoverthelazydog",
        )

    def test_decode_all_the_letters2(self):
        self.assertEqual(
            decode("kqlfd jzvgy tpaet icdhm rtwly kqlon ubstx", 19, 13),
            "thequickbrownfoxjumpsoverthelazydog",
        )

    def test_decode_with_no_spaces_in_input1(self):
        self.assertEqual(
            decode("swxtjnpvyklruoliejdcblaxkswxmhqzglf", 17, 33),
            "thequickbrownfoxjumpsoverthelazydog",
        )

    def test_decode_with_no_spaces_in_input2(self):
        self.assertEqual(
            decode("AnObstacleIsOftenASteppingStone", 23, 31),
            "tgxknetbyjznxaejgtnejoozgrnexgj",
        )

    def test_decode_with_too_many_spaces(self):
        self.assertEqual(
            decode("vszzm    cly   yd cg    qdp", 15, 16), "jollygreengiant"
        )

    def test_decode_with_a_not_coprime_to_m(self):
        with self.assertRaisesWithMessage(ValueError):
            decode("Test", 13, 5)

    def test_decode_with_a_not_coprime_to_m_2(self):
        with self.assertRaisesWithMessage(ValueError):
            decode("ybty", 18, 13)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
