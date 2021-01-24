from typing import List, Tuple
import functools

## decorator
def check_factors(fn):
    @functools.wraps(fn)
    def wrapped_fn(*args, **kwargs):
        ((k1, min_f), (k2, max_f)) = kwargs.items()
        assert k1 == 'min_factor' and k2 == 'max_factor' or \
            k1 == 'max_factor' and k2 == 'min_factor'
        if max_f < min_f:
            raise ValueError(f'min. factor: {min_f} must be < max. factor: {max_f}')
        return fn(*args, **kwargs)
    #
    return wrapped_fn


@check_factors
def largest(min_factor: int, max_factor: int) -> List[Tuple[int, int]]:
    a = gen_palindrome_product(min_factor, max_factor)
    return a[-1] if len(a) > 0 else [None, ()]

@check_factors
def smallest(min_factor: int, max_factor: int) -> List[Tuple[int, int]]:
    a = gen_palindrome_product(min_factor, max_factor)
    return a[0] if len(a) > 0 else [None, ()]

##
## Internal Helpers
##

def is_palindrome(p: int) -> bool:
    sp = str(p)
    n = len(sp)
    for ix in range(n // 2):
        if sp[ix] != sp[n - 1 - ix]: return False
    return True


def gen_palindrome_product(a: int, b: int) -> List[Tuple[int, int]]:
    """
    a: min_factor
    b: max_factor
    """
    hsh = {}
    for x in range(a, b+1):
        for y in range(x, b+1):
            p = x * y
            if is_palindrome(p):
                l = hsh.get(p, [])
                l.append((x, y))
                hsh[p] = l
    ##
    # l = sorted(list(hsh.items()), key=lambda t: t[0])
    # return list(map(lambda t: (t[0], sorted(t[1], key=lambda st: (st[0], st[1]))), l))
    return sorted(list(hsh.items()), key=lambda t: t[0])

def gen_palindrome_product_OLD(a: int, b: int) -> List[Tuple[int, int]]:
    """
    a: min_factor
    b: max_factor
    """
    return sorted(
        [
            (x * y, [(x, y)]) for x in range(a, b+1) for y in range(x, b+1) if is_palindrome(x * y)
        ],
        key=lambda t: (t[0], t[1][0][0], t[1][0][1])
    )
