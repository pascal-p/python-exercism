import unittest

from sgf_parsing import parse, SgfTree

# Tests adapted from `problem-specifications//canonical-data.json`


class SgfParsingTest(unittest.TestCase):

    def test_empty_input(self):
        input_string = ""
        with self.assertRaisesWithMessage(ValueError):
            parse(input_string)

    def test_tree_with_no_nodes(self):
        input_string = "()"
        with self.assertRaisesWithMessage(ValueError):
            parse(input_string)

    def test_node_without_tree(self):
        input_string = ";"
        with self.assertRaisesWithMessage(ValueError):
            parse(input_string)

    def test_all_lowercase_property(self):
        input_string = "(;a[b])"
        with self.assertRaisesWithMessage(ValueError):
            parse(input_string)

    def test_node_without_properties(self):
        input_string = "(;)"
        expected = SgfTree()
        self.assertEqual(parse(input_string), expected)

    def test_single_node_tree(self):
        input_string = "(;A[B])"
        expected = SgfTree(properties={"A": ["B"]})
        self.assertEqual(parse(input_string), expected)

    def test_multiple_properties(self):
        input_string = "(;A[b]C[d])"
        expected = SgfTree(properties={"A": ["b"], "C": ["d"]})
        self.assertEqual(parse(input_string), expected)

    def test_properties_without_delimiter(self):
        input_string = "(;A)"
        with self.assertRaisesWithMessage(ValueError):
            parse(input_string)

    def test_upper_and_lowercase_property(self):
        input_string = "(;Aa[b])"
        with self.assertRaisesWithMessage(ValueError):
            parse(input_string)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
