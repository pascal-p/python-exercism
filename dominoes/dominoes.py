"""
   Dominoes
"""

from typing import List, Tuple


def can_chain(dominoes: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if len(dominoes) == 0:
        return []
    elif len(dominoes) == 1:
        return dominoes if dominoes[0][0] == dominoes[0][1] else None

    # enumerating and stop at first success
    cpy_dominoes = [*dominoes]
    for domino in dominoes:
        cpy_dominoes.remove(domino)
        res, chain = find_chain(cpy_dominoes, [domino], len(dominoes), 1)
        if res:
            return chain
        # else try another candidate
        cpy_dominoes = [*dominoes]
    # if we end up here, then failure
    return None


def find_chain(dominoes: List[Tuple[int, int]], chain: List[Tuple[int, int]],
               n: int, p: int) -> Tuple[bool, List[Tuple[int, int]]]:
    """
    Try to find a chain by enumerating all possible orders
    Note: we can swap the order of the values of a dominoe ex. (3, 1) -> (1, 3)
    """
    if len(dominoes) == 0 and len(chain) == n:
        return (True, chain) if chain[0][0] == chain[-1][1] else (False, [])
    elif len(dominoes) == 0:
        return (False, [])
    #
    curr = chain[-1]
    candidates = find_next(dominoes, curr)
    if len(candidates) == 0:
        if chain[0][0] == dominoes[0][1] and chain[-1][1] == dominoes[0][0]:
            chain.append(dominoes[-1])
            return (True, chain) if len(chain) == n else (False, [])
        return (False, [])
    #
    while len(candidates) > 0:
        cand = candidates[0]
        remove(dominoes, cand)
        candidates = candidates[1:]
        res, fchain = find_chain(dominoes, [*chain, cand], n, p + 1)
        if res:
            return (res, fchain)
        # try another candidate
        dominoes.append(cand)
    #
    # if we get here => failure
    return (False, [])


def remove(dominoes: List[Tuple[int, int]], domino: Tuple[int, int]):
    """
       As we can swap the order of a domino, we need to take some precautions
    when removing a domino from the list
    """
    try:
        dominoes.remove(domino)
    except ValueError:
        # domino was swapped, ex (1, 3) -> (3, 1)
        # we need to restore the initial order
        dominoes.remove((domino[1], domino[0]))


def find_next(dominoes: List[Tuple[int, int]], domino: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    >>> find_next([(2, 3), (3, 1), (2, 4), (2, 4)], (1, 2))
    ((1, 2), [(2, 3), (2, 4)])

    >>> find_next([(2, 3), (3, 1), (2, 4), (2, 4)], (2, 1))
    ((1, 2), [(2, 3), (2, 4)])
    """
    s = set(
        d for d in dominoes if domino[1] == d[0]
    )
    if len(s) == 0:
        # try alternative - swap order of current (domino)
        s = set(
            (d[1], d[0]) for d in dominoes if domino[1] == d[1]
        )
    return list(s)
