from typing import List, Tuple

VALID_CHARS =  (' ', '*')

def annotate(minefield):
    nr = len(minefield)
    if nr <= 0: return minefield

    nc = len(minefield[0])
    if nc == 0: return minefield

    check_same_len_lines(minefield, nc)

    if all_empty(minefield, nr, nc) or all_stars(minefield, nr, nc):
        return minefield

    check_non_valid_chars(minefield, nr, nc)

    for r in range(nr):
        line = ''
        for c in range(nc):
            if minefield[r][c] == VALID_CHARS[1]:
                line += VALID_CHARS[1]  ## '*'
                continue
            ##
            ## now, count the number of mine(s) in neighborhood
            cnt = 0
            for (x, y) in neighbors(r, c, nr, nc):
                # assert 0 <= x < nr and 0 <= y < nc
                if minefield[x][y] == VALID_CHARS[1]: cnt += 1
            if cnt > 0:
                line += f"{cnt}"
            else:
                line += minefield[r][c]
        minefield[r] = line
    return minefield

def check_same_len_lines(minefield, nc):
    "check if all lines have same length"
    m = list(filter(lambda l: len(l) != nc, minefield))
    if len(m) > 0:
        raise ValueError("lines must have the same length")
    return

def all_empty(minefield, nr, nc) -> bool:
    "check if all lines are empty"
    m = list(filter(lambda l: l == VALID_CHARS[0] * nc, minefield))
    return len(m) == nr

def all_stars(minefield, nr, nc) -> bool:
    "check if all lines contain only '*'"
    m = list(filter(lambda l: l == VALID_CHARS[1] * nc, minefield))
    return len(m) == nr

def check_non_valid_chars(minefield, nr, nc):
    "check fro invalid chars"
    for lines in minefield:
        for ch in lines:
            if not ch in VALID_CHARS:
                raise ValueError("invalid char found")
    return

# return a generator
def neighbors(row:int, col:int, nr:int, nc:int):
    return (
        (r, c) for r in range(row-1, row+2) if 0 <= r < nr
        for c in range(col-1, col+2) if 0 <= c < nc and not (r == row and c == col)
    )
