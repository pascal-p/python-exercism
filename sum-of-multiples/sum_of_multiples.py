from typing import List

def sum_of_multiples(limit: int, multiples:List[int]) -> int:
    hsh = {0: 1}
    for m in multiples:
        if m == 0: continue

        for p in range(m, limit, m):
            if p in hsh: continue
            hsh[p] = 1

    return sum(hsh.keys())

# if we don't care about repetition:
# som = 0
# som += sum((p for p in range(m, limit, m)))   ## generator() rather than a list[]
