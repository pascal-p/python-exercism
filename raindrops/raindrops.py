"""
   Raindrops Exo
"""

from typing import List

MAP = {
    3: 'Pling',
    5: 'Plang',
    7: 'Plong'
}

FACTORS = [k for k in MAP.keys()]


def convert(number: int) -> str:
    if number < -1:
        return str(number)
    if number in FACTORS:
        return MAP[number]
    res = decomp(number)
    return str(number) if len(res) == 0 else "".join(res)


def decomp(num: int) -> List[str]:
    res, ix = [], 0
    while ix < len(FACTORS):
        f = FACTORS[ix]
        if num % f == 0:
            res.append(MAP[f])
        while num % f == 0:
            num //= f
        ix += 1
    return res
