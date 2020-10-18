import re

VALID_SUBSTR = [str(x) for x in range(10)] + ['X']
BASE_ISBN13 = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
ISBN_LEN = 10
ISBN13_LEN = 13

ISBN_REXP = r"\A\d\-?\d{3}\-?\d{5}\-?(\d|X)\Z"
ISBN13_REXP = r"\A\d{13}\Z"


class ISBN:
    def __init__(self, str=None):
        if not self._is_valid(str):
            raise ValueError("Not a valid ISBN")
        self.isbn = self._norm(str)

    def build_isbn10_from_prefix(self, prefix: str) -> str:
        # TODO
        pass

    def build_isbn13_from_prefix(self, prefix: str) -> str:
        # TODO
        pass

    def _norm(self, isbn:str) -> str:
        return ''.join(isbn.split('-'))

    def _is_valid(self, cisbn: str) -> bool:
        "wrapper for _is_valid10 and _is_valid13..."

        if len(cisbn) not in [ISBN_LEN, ISBN13_LEN, ISBN13_LEN + 4]:
            return False

        isbn = self._norm(cisbn)

        if len(isbn) == ISBN_LEN: return self._is_valid10(isbn)
        elif len(isbn) == ISBN13_LEN: return self._is_valid13(isbn)
        return False

    def _is_valid13(self, cisbn: str) -> bool:
        if not re.match(ISBN13_REXP, cisbn):
            return False
        res = self._checksum(cisbn)
        if res == -1: Falss
        return str(res) == cisbn[-1]

    def _is_valid10(self, cisbn: str) -> bool:
        if not re.match(ISBN_REXP, cisbn, re.IGNORECASE):
            return False

        s = sum([int(ch) * (10 - ix) if '0' <= ch <= '9' else 10 \
                 for ix, ch in enumerate(cisbn)])

        return s % 11 == 0

    def _checksum(self, cisbn):
        s = sum([
          int(sd) * b for sd, b in zip(list(cisbn)[:-1], BASE_ISBN13[:-1])
        ])
        return (10 - s % 10) % 10


def is_valid(isbn):
    try:
        _isbn = ISBN(isbn)
        return True

    except ValueError  as _err:
        return False
