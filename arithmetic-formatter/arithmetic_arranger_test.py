import unittest

from arithmetic_arranger import arithmetic_arranger


# the test case
class UnitTests(unittest.TestCase):
    def test_arrangement(self):
        actual = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]')

        actual = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
        expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]')

    def test_too_many_problems(self):
        actual = arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
        expected = "Error: Too many problems."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with more than five problems to return "Error: Too many problems."')

    def test_incorrect_operator(self):
        actual = arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Operator must be '+' or '-' or 'x'."
        self.assertEqual(actual, expected, '''Expected calling "arithmetic_arranger()" with a problem that uses the "/" operator to return "Error: Operator must be '+' or '-'."''')

    def test_too_many_digits(self):
        actual = arithmetic_arranger(["24 + 85215", "3801 - 21234567", "45 + 43", "123 + 49"])
        expected = "Error: Numbers cannot be more than six digits."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with a problem that has a number over 4 digits long to return "Error: Numbers cannot be more than four digits."')

    def test_only_digits(self):
        actual = arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers must only contain digits."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."')

    def test_solutions(self):
        actual = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
        expected = "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"
        self.assertEqual(actual, expected, 'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with arithemetic problems and a second argument of `True`.')

    # EXTENSION
    # def test_add_sub_mult_expr(self):
    #     actual = arithmetic_arranger(['32 + 448', '448 - 32', '1121 + 999', '123 x 44', '32 - 448'], True)
    #     expected = "\n".join([
    #         " -----    ----    -----    -----    -----",
    #         "   480     416     2120      492     -416",
    #         "                            492.         ",
    #         "                           -----         ",
    #         "                            5412         ",
    #     ])
    #     pass

    # def test_mult_solutions(self):
    #     actual = arithmetic_arranger(["999999 x 999999", "999999 x 999999",
    #                                   "999999 x 999999", "999999 x 999999", "999999 x 999999"], True)
    #     expected = "\n".join([
    #         "------------   ------------   ------------   ------------   ------------   ------------",
    #         "     8999991        8999991        8999991        8999991        8999991        8999991",
    #         "    8999991.       8999991.       8999991.       8999991.       8999991.       8999991.",
    #         "   8999991..      8999991..      8999991..      8999991..      8999991..      8999991..",
    #         "  8999991...     8999991...     8999991...     8999991...     8999991...     8999991...",
    #         " 8999991....    8999991....    8999991....    8999991....    8999991....    8999991....",
    #         "8999991.....   8999991.....   8999991.....   8999991.....   8999991.....   8999991.....",
    #         "------------   ------------   ------------   ------------   ------------   ------------",
    #         "999998000001   999998000001   999998000001   999998000001   999998000001   999998000001"
    #     ])
    #     self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()


#    32     448     1121      123       32
# + 448    - 32    + 999    x  44    - 448
# -----    ----    -----    -----    -----
#   480     416     2120      492     -416
#                            492.
#                           -----
#                            5412


#       999999         999999         999999         999999         999999         999999
# x     999999   x     999999   x     999999   x     999999   x     999999   x     999999
# ------------   ------------   ------------   ------------   ------------   ------------
#      8999991        8999991        8999991        8999991        8999991        8999991
#     8999991.       8999991.       8999991.       8999991.       8999991.       8999991.
#    8999991..      8999991..      8999991..      8999991..      8999991..      8999991..
#   8999991...     8999991...     8999991...     8999991...     8999991...     8999991...
#  8999991....    8999991....    8999991....    8999991....    8999991....    8999991....
# 8999991.....   8999991.....   8999991.....   8999991.....   8999991.....   8999991.....
# ------------   ------------   ------------   ------------   ------------   ------------
# 999998000001   999998000001   999998000001   999998000001   999998000001   999998000001
