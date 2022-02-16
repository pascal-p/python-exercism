"""
    Darts Exo
"""

import math


def score(x: float, y: float) -> int:
    d = euclidean_dist(x, y)
    if d > 10.0:
        return 0
    elif d > 5.0:
        return 1
    elif d > 1.0:
        return 5
    else:
        return 10


def euclidean_dist(x: float, y: float) -> float:
    return math.sqrt(x ** 2 + y ** 2)
