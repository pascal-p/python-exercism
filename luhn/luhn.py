import re
import functools

class Luhn:
    def __init__(self, card_num):
        self.card_num = re.sub(r'[\s\t\n\r]+', '', card_num)

    def valid(self):
        if len(self.card_num) <= 1:                               # check length
            return False

        if not re.match(r'\A[0-9]+\Z', self.card_num):            # consider only digits
            return False

        return self._extract_calc(list(self.card_num)) % 10 == 0  # calculate and conclude

    def _extract_calc(self, ary):
        """
        Do not build array => too expensive
        Extract, double and sum every 2nd digit while extractimg and summing every 1st digit
        return sum of these two sums
        """
        r = 0 if len(ary) % 2 == 0 else 1

        def reducer_fn(csum, t):
            """
              closure
              t == tuple(ix, ch)
            """
            ix, d = t[0], int(t[1])
            if ix % 2 == r:
                x = 2 * d
                csum[1] += x - 9 if x > 9 else x
            else:

                csum[0] += d
            return csum

        foldl = lambda fn, acc, xs: functools.reduce(fn, xs, acc)

        res = foldl(reducer_fn, [0, 0], enumerate(ary))
        return sum(res)
