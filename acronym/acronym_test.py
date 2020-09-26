import unittest

from acronym import abbreviate

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.7.0


class AcronymTest(unittest.TestCase):
    def test_basic1(self):
        self.assertEqual(abbreviate(""), "")

    def test_basic2(self):
        for s, exp in [
                ("Portable Network Graphics", "PNG"),
                ("Looks good to me", "LGTM"),
                ("Sounds 'good' to me", "SGTM"),
                ("Isn't it good", "IIG"),
                ("If and only if...", "IAOI"),
                ("Yet Another Funny Acronym", "YAFA"),
                ("Sometimes, it is necessary to raise an exception.", "SIINTRAE"),
                ("Last-in, first-out", "LIFO"),
                ('Oh my "Gosh!"', "OMG"),
                ("Functional Programming", "FP"),
                ("Imperative Programming", "IP"),
                ("Object oriented Programming", "OOP"),
                ("Differentiable Programming", "DP")
        ]:
            self.assertEqual(abbreviate(s), exp)

    def test_lowercase_words(self):
        self.assertEqual(abbreviate("Ruby on Rails"), "ROR")

    def test_punctuation(self):
        self.assertEqual(abbreviate("First In, First Out"), "FIFO")

    def test_all_caps_word(self):
        self.assertEqual(abbreviate("GNU Image Manipulation Program"), "GIMP")

    def test_punctuation_without_whitespace(self):
        self.assertEqual(abbreviate("Complementary metal-oxide semiconductor"), "CMOS")

    def test_very_long_abbreviation(self):
        self.assertEqual(
            abbreviate(
                "Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me"
            ),
            "ROTFLSHTMDCOALM",
        )

    def test_consecutive_delimiters(self):
        self.assertEqual(abbreviate("Something - I made up from thin air"), "SIMUFTA")

    def test_apostrophes(self):
        self.assertEqual(abbreviate("Halley's Comet"), "HC")

    def test_underscore_emphasis(self):
        self.assertEqual(abbreviate("The Road _Not_ Taken"), "TRNT")


if __name__ == "__main__":
    unittest.main()
