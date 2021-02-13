from typing import List

def spiral_matrix(size: int) -> List[List[int]]:
    k, u, v = 0, 0, size

    # closure:
    def incr():
      nonlocal k
      k += 1
      return k

    ## init matrix with zeros
    m = [[0 for _ in range(size)] for _ in range(size)]
    #
    while u < v:
        for c in range(u, v):             ## fill from left/right
            m[u][c] = incr()

        for r in range(u + 1, v):         ## fill right top/down
            m[r][v - 1] = incr()

        for c in range(v - 2, u - 1, -1): ## fill right/left
            m[v - 1][c] = incr()

        for r in range(v - 2, u, -1):     ## fill left bottom/up
            m[r][u] = incr()

        u += 1
        v -= 1
        #
    return m
