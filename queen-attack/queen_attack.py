BOARD_DIM = 8

class Queen:
    def __init__(self, row, column):
        check_coord(row, column)
        self._r = row
        self._c = column
        self._du = (-1, row + column)  ## equation of diagonal up (r + i, c - i) .. (r - i, c + i)
        self._dd = (1, row - column)   ## equation of diagonal down (r - i, c - i) .. (r + i, c + i)

    def can_attack(self, oq):
        if self.get_pos() == oq.get_pos():
            raise(ValueError("other queen cannot be at the same position"))

        return self.same_row(oq) or self.same_col(oq) or self.same_diag(oq)

    def get_pos(self):
        return (self._r, self._c)

    def same_col(self, oq):
        return self._c == oq._c

    def same_row(self, oq):
        return self._r == oq._r

    def same_diag(self, oq):
        return oq._r == self._du[0] * oq._c + self._du[1] or \
            oq._r == self._dd[0] * oq._c + self._dd[1]

def check_coord(r, c):
    for x in (r, c):
        if not inbounds(x):
            raise(ValueError("Position not in given board"))
    return

def inbounds(x: int) -> bool:
    return 0 <= x < BOARD_DIM
