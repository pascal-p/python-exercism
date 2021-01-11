class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        assert len(puzzle) > 0
        self.puzzle = puzzle
        self.dim = (len(puzzle), len(puzzle[0]))

    def search(self, word):
        start_p, end_p = None, None
        nr, nc = self.dim
        rix, cix = 0, 0

        while rix < nr:
            ((r, c), cix) = self.find_1st(word, rix, cix)

            if r is not None and c is not None:
                start_p = Point(c, r)
                found_2nd = False

                for (kx, (r, c)) in enumerate(self.neighbors(start_p)):
                    if not (0 <= c < nc and 0 <= r < nr and (r != start_p.y or c != start_p.x)):
                        continue

                    if word[1] == self.puzzle[r][c]:
                        found_2nd = True

                    if found_2nd:
                        (lr, lc) = self.match(word, kx, r, c)
                        if lr is not None and lc is not None:
                            end_p = Point(lc, lr)
                            return (start_p, end_p)

                        else:
                            found_2nd = False  ## try next neighbor
            ##
            cix += 1      ## Failure after 2nd match try again, on next column...
            if cix > nc:
                cix = 0
                rix += 1  ## ...or next line
        ##
        return None

    def find_1st(self, word, r=0, c=0):
        cix = c
        for ch in self.puzzle[r][c:]:
            if ch == word[0]:
                return ((r, cix), cix)  ## found first match
            cix += 1
        return ((None, None), cix)

    def match(self, word, kx, r, c):
        """
        #
        # NOTE kx == 0 => means \     (r - 1, c - 1)
        #      kx == 1 => means |     (r - 1, c)
        #      kx == 2 => means /     (r - 1, c + 1)
        #      kx == 3 => means -(L)  (r, c - 1)
        #      kx == 5 => means -(R)  (r, c + 1)
        #      kx == 6 => means /     (r + 1, c - 1)
        #      kx == 7 => means |     (r + 1, c)
        #      kx == 8 => means \     (r + 1, c + 1)
        #
        """
        m = len(word) - 1
        ix = 1
        nr, nc = (None, None)

        if kx == 0:
            for jx in range(1, m): #len(self.puzzle)):
                if word[ix + jx] != self.puzzle[r - jx][c - jx]:
                    return (nr, nc)
            nr, nc = (r - m + 1, c - m + 1)
        #
        elif kx == 1:
            for jx in range(1, m):
                if word[ix + jx] != self.puzzle[r - jx][c]:
                    return (nr, nc)
            nr, nc = (r - m + 1, c)
        #
        elif kx == 2:
            for jx in range(1, m):
                if word[ix + jx] != self.puzzle[r - jx][c + jx]:
                    return (nr, nc)
            nr, nc = (r - m + 1, c + m - 1)
        #
        elif kx == 3:
            for jx in range(1, m):
                if word[ix + jx] != self.puzzle[r][c - jx]:
                    return (nr, nc)
            nr, nc = (r, c - m + 1)
        #
        elif kx == 5:
            for jx in range(1, m):
                if word[ix + jx] != self.puzzle[r][c + jx]:
                    return (nr, nc)
            nr, nc = (r, c + m - 1)
        #
        elif kx == 6:
            for jx in range(1, m):
                if word[ix + jx] != self.puzzle[r + jx][c - jx]:
                    return (nr, nc)
            nr, nc = (r + m - 1, c - m + 1)
        #
        elif kx == 7:
            for jx in range(1, m):
                if word[ix + jx] != self.puzzle[r + jx][c]:
                    return (nr, nc)
            nr, nc = (r + m - 1, c)
        #
        elif kx == 8:
            for jx in range(1, m):
                if word[ix + jx] != self.puzzle[r + jx][c + jx]:
                    return (nr, nc)
            nr, nc = (r + m - 1, c + m - 1)

        return (nr, nc)

    def neighbors(self, pt:Point):
        x, y = pt.x, pt.y

        return [(r, c) for r in range(y - 1, y + 2)
                for c in range(x - 1, x + 2)]
