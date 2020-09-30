import functools
import re
from typing import Tuple

STR = 'abcdefghijklmnopqrstuvwxyz'
M = len(STR)
L2IX = { k: v for k, v in zip('abcdefghijklmnopqrstuvwxyz', range(M)) }
IX2L = { v: k for k, v in L2IX.items() }
NON_ALPHA_REXP = r'[^a-zA-Z0-9]'
GRP_SIZE = 5 + 1 # + 1 for space


##
## utilities
##

def _xgcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended GCD(a, b) == a * x + b * y == g

    here b will be 26 (always), g is 1 thus find (x, y) relative integer (Z)
    such that a (> 0) * x + 26 * y == 1

    ref. https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
         https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    """
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def _gcd(a: int, b: int) -> int:
    # a > 0 and b > 0
    a, b = (b, a) if a < b else (a, b)
    if b == 0: return a
    r = a
    while r > 1:
        r = a % b
        a, b = b, r
    return a if r == 0 else r

def _is_coprime(a: int) -> bool:
    """
    are (a, M) coprime?
    """
    return _gcd(a, M) == 1

def check_coprime(fn):
    @functools.wraps(fn)
    def wrapper_fn(*args, **kwargs):
        _, a, _ = args
        if not _is_coprime(a):
            raise ValueError(f'a {a} and m {M} must be coprimes')
        res = fn(*args, **kwargs)
        return res

    return wrapper_fn

def grouping(s: str, ch: str) -> str:
    l = len(s) + 1  # as ch is a latin char (actually a string)
    return s + ch + ' ' if l % GRP_SIZE == 0 else s + ch

##
## API (public)
##

@check_coprime
def encode(plain_text: str, a: int, b: int) -> str:
    """
    E(x) = (a * x + b) % M
    """
    def encode_fn(x):
        return IX2L[(a * L2IX[x.lower()] + b) % M] if not ('0' <= x <= '9') else x

    ary = map(encode_fn,
              filter(lambda x: not re.match(NON_ALPHA_REXP, x),
                     list(plain_text)))

    return functools.reduce(lambda s, c: grouping(s, c),
                            ary,
                            ' ').strip()

@check_coprime
def decode(ciphered_text: str, a: int, b: int) -> str:
    """
    D(y) = a^-1(y - b) mod m, where y = E(x) and a^-1 is MMI of a

    MMI == Modular Multiplicative Inverse, it can be found using the
    extended Euclidean algorithm (xgcd)
    """
    inv_a = _xgcd(a, M)[1]

    def decode_fn(x):
        return IX2L[(inv_a * (L2IX[x.lower()] - b)) % M] if not ('0' <= x <= '9') else x

    return ''.join(map(decode_fn,
                       filter(lambda x: not re.match(NON_ALPHA_REXP, x),
                              list(ciphered_text))))
