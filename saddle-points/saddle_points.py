import sys
from typing import List

def saddle_points(matrix: List[List[int]]):
    nrows = len(matrix)

    if nrows == 0: return []
    check_irregular_matrix(matrix, nrows)

    sp = []
    for r in range(nrows):
        for c in range(len(matrix[r])):
            if matrix[r][c] == max(matrix[r]) and \
               matrix[r][c] == min([matrix[r][c] for r in range(nrows)]):
                sp.append({"row": r + 1, "column": c + 1})

    return sorted(sp, key=lambda h: (h["row"], h["column"]))

def check_irregular_matrix(matrix, nrows):
    len0 = len(matrix[0])
    for r in range(1, nrows):
        if len(matrix[r]) != len0:
            raise ValueError("Irregular matrix detected")
    return

#
# A longer attempt...
#
def saddle_points_ALT(matrix: List[List[int]]):
    nrows = len(matrix)

    if nrows == 0: return []
    check_irregular_matrix(matrix, nrows)

    sp = []
    s = - sys.maxsize - 1
    ir, ic = -1, -1
    witness = False

    if nrows == 1:
        for c in range(len(matrix[0])):
            if matrix[0][c] > s:
                s = matrix[0][c]
                ic = c

            if matrix[0][c] == s and c != ic:
                sp.append({"row": 1, "column": ic + 1})
                witness = True
                ic = c

        if witness:
            fs = {"row": 1, "column": ic + 1}
            if fs not in sp: sp.append(fs)
        return sp

    for r in range(0, 1):
        for c in range(len(matrix[0][:])):
            if matrix[r][c] > s:
                s = matrix[r][c]
                ir = r
                ic = c

            # other columns
            for c in range(len(matrix[0])):
                if c == ic: continue
                if matrix[0][c] == s:
                    if matrix[0][c] == min([matrix[r][c] for r in range(nrows)]):
                        # make sure, prev. s was actually a saddle point
                        if matrix[0][ic] == min([matrix[r][ic] for r in range(nrows)]):
                            append_cond(sp, 0, ic)
                        ic = c

    for r in range(1, nrows):
        if matrix[r][ic] < s:
            if matrix[r][ic] >= max(matrix[r]):
                witness = True
                s = matrix[r][ic]
                ir = r

        elif matrix[r][ic] == s:   # tie
            if matrix[r][ic] >= max(matrix[r]):
                append_cond(sp, ir, ic)
                witness = True
                ir = r

        # other columns, same row
        for c in range(len(matrix[ir])):
            if c == ic: continue
            if matrix[ir][c] == s:
                if matrix[ir][c] == min([matrix[r][c] for r in range(nrows)]):
                    append_cond(sp, ir, ic)
                    ic = c

    if witness: append_cond(sp, ir, ic)
    return sorted(sp, key=lambda h: (h["row"], h["column"]))

def append_cond(sp, ir, ic):
    fs = {"row": ir + 1, "column": ic + 1}
    if fs not in sp: sp.append(fs)
    return
