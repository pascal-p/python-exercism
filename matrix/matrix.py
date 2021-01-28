import re

class Matrix:
    def __init__(self, matrix_string: str):
        assert len(matrix_string) > 0
        ary = matrix_string.split("\n")
        self.content = [[] for _r in ary]
        for ix, row in enumerate(ary):
            self.content[ix] = [
                int(r) for r in re.split('\s+', row)
            ]
        self.shape = (len(self.content), len(self.content[0]))

    def row(self, ix: int):
        assert 0 <= ix - 1 < self.shape[0]
        return self.content[ix - 1]

    def column(self, ix: int):
        assert 0 <= ix - 1 < self.shape[1]
        return [
            r[ix - 1] for r in self.content
        ]
