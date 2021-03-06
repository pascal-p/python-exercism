from typing import List# , Tuple

L_Int = List[int]
L_Bool = List[bool]

MAX_PRIME_LIM = 10_000

# not satisfactory => not efficient!

def prime(num: int, lim=MAX_PRIME_LIM) -> int:
    if not 0 < num < lim:
        raise ValueError("Not in acceptable interval")
    #
    _primes = gen_primes_lt(lim)
    # alt:  _primes = list(gen_primes(MAX_PRIME_LIM))
    return _primes[num - 1]


def gen_primes_lt(n: int) -> L_Int:
    prime_ind = [True] + [
        True for _ in range(1, (n - 4) // 2 + 1) # range(3, n - 1, 2)
    ]                                        # gen. list of candidate prime [3, 5, 7, ...]...
    #                                        # ... a priori primes (set to True)
    ix, m = 0, len(prime_ind)
    while ix < m:
        cp = 2 * ix + 3                      # candidate prime cp from 3, 5, 7, 11...
        for jx in range(ix + cp, m, cp):     # mark multiples of cp as non prime (sieve method)
            prime_ind[jx] = False
        #
        ix += 1                              # set ix to next (candidate) prime
        while ix < m and not prime_ind[ix]:
            ix += 1
    #
    return [2] + [
        2 * ix + 3 for ix in range(m) if prime_ind[ix]
    ]                                        # return computed list of prime adding 2 (the only even int to be prime)


#
# Alt. an attempt with generator
#
def gen_primes(n:int):
    ix = 0
    primes, prime_ind = gen_primes_hlpr(n)

    while True:
        next_prime = primes[-1]
        yield next_prime

        if ix is None: return
        ix = gen_next_primes(ix, primes, prime_ind)
    #
    return

def gen_primes_hlpr(n: int):
    """
    cp    3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51
    flag  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T
    ix    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
    """
    primes = [2]
    prime_ind = [True] + [
        True for cp in range(3, n - 1, 2)
    ]
    return (primes, prime_ind)

def gen_next_primes(ix:int, primes:L_Int, prime_ind:L_Bool) -> int:
    if ix >= len(prime_ind):
        return None

    cp = 2 * ix + 3
    for jx in range(ix + cp, len(prime_ind), cp):
        prime_ind[jx] = False

    primes += [cp]

    ix += 1
    while ix < len(prime_ind) and not prime_ind[ix]:
        ix += 1

    if ix >= len(prime_ind):
        return None

    return ix
