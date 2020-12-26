import unittest

from satellite import tree_from_traversals

# Tests adapted from `problem-specifications//canonical-data.json`


class SatelliteTest(unittest.TestCase):
    def test_empty_tree(self):
        preorder = []
        inorder = []

        expected = {}
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_tree_with_one_item(self):
        preorder = ["a"]
        inorder = ["a"]

        expected = {"v": "a", "l": {}, "r": {}}
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_tree_with_many_items(self):
        preorder = ["a", "i", "x", "f", "r"]
        inorder = ["i", "a", "f", "x", "r"]

        expected = {
            "v": "a",
            "l": {"v": "i", "l": {}, "r": {}},
            "r": {
                "v": "x",
                "l": {"v": "f", "l": {}, "r": {}},
                "r": {"v": "r", "l": {}, "r": {}},
            },
        }
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_tree_with_many_more_items1(self):
        preorder = ['f', 'b', 'a', 'd', 'c', 'e', 'g', 'i', 'h']
        inorder = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        #
        #
        # . . . . F . . . .
        #      /    \
        # . B . . .  G
        # /  \        \
        # A . D . . .  I
        #    / \      /
        # . C . E . H
        #
        expected = {
            "v": "f",
            "l": {"v": "b",
                  "l": {"v": "a", "l": {}, "r": {}},
                  "r": {"v": "d",
                        "l": {"v": "c", "l": {}, "r": {}},
                        "r": {"v": "e", "l": {}, "r": {}}}},
            "r": {
                "v": "g",
                "l": {},
                "r": {"v": "i",
                      "l": {"v": "h", "l": {}, "r": {}},
                      "r": {}},
            },
        }
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_tree_with_many_more_items2(self):
        preorder = ['+', '*', 'a', '-', 'b', 'c', '/', 'd', 'e']
        inorder = ['a', '*', 'b',  '-', 'c', '+',  'd', '/',  'e']
        expected = {
            "v": "+",
            "l": {"v": "*",
                  "l": {"v": "a", "l": {}, "r": {}},
                  "r": {"v": "-",
                        "l": {"v": "b", "l": {}, "r": {}},
                        "r": {"v": "c", "l": {}, "r": {}}},
                  },
            "r": {
                "v": "/",
                "l": {"v": "d", "l": {}, "r": {}},
                "r": {"v": "e", "l": {}, "r": {}},
            },
        }
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_reject_traversals_of_different_length(self):
        preorder = ["a", "b"]
        inorder = ["b", "a", "r"]

        with self.assertRaisesWithMessage(ValueError):
            tree_from_traversals(preorder, inorder)

    def test_reject_inconsistent_traversals_of_same_length(self):
        preorder = ["x", "y", "z"]
        inorder = ["a", "b", "c"]

        with self.assertRaisesWithMessage(ValueError):
            tree_from_traversals(preorder, inorder)

    def test_reject_traversals_with_repeated_items(self):
        preorder = ["a", "b", "a"]
        inorder = ["b", "a", "a"]

        with self.assertRaisesWithMessage(ValueError):
            tree_from_traversals(preorder, inorder)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
