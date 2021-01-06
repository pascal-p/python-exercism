import unittest

from sgf_parsing import parse, SgfTree

# Tests adapted from `problem-specifications//canonical-data.json`


class SgfParsingTest(unittest.TestCase):

    def test_two_nodes(self):
        input_string = "(;A[B];B[C])"
        expected = SgfTree(properties={"A": ["B"]},
                           children=[
                               SgfTree({"B": ["C"]})
                           ])
        self.assertEqual(parse(input_string), expected)

    def test_two_child_trees(self):
        input_string = "(;A[B](;B[C])(;C[D]))"
        expected = SgfTree(
            properties={"A": ["B"]},
            children=[
                SgfTree({"B": ["C"]}),
                SgfTree({"C": ["D"]})
            ],
        )
        self.assertEqual(parse(input_string), expected)

    def test_multiple_property_values(self):
        input_string = "(;A[b][c][d])"
        expected = SgfTree(
            properties={"A": ["b", "c", "d"]}
        )
        self.assertEqual(parse(input_string), expected)

    def test_escaped_property(self):
        input_string = "(;A[\\]b\nc\nd\t\te \n\\]])"
        expected = SgfTree(
            properties={"A": ["]b\nc\nd  e \n]"]}
        )
        self.assertEqual(parse(input_string), expected)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
