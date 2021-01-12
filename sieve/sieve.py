from typing import List, Tuple
import math

PRIME_FACT_LT20 = [2, 3, 5, 7, 11, 13, 17, 19]

def primes(limit:int) -> List[int]:
    if limit <= 1:
        return []
    if limit <= 2:
        return PRIME_FACT_LT20[0:1]
    elif limit <= 4:
        return PRIME_FACT_LT20[0:2]
    elif limit <= 6:
        return PRIME_FACT_LT20[0:3]
    elif limit <= 10:
        return PRIME_FACT_LT20[0:4]
    elif limit <= 12:
        return PRIME_FACT_LT20[0:5]
    elif limit <= 16:
        return PRIME_FACT_LT20[0:6]
    elif limit <= 18:
        return PRIME_FACT_LT20[0:7]
    elif limit <= 20:
        return PRIME_FACT_LT20[0:7]

    # Extend primes list
    cprimes = [
        (ix, True) for ix in range(23, limit, 2)
    ]

    ncp = len(cprimes)
    primes = PRIME_FACT_LT20.copy()
    terminated = False
    kxp, cix = 1, 0

    while True:
        p, kxp = next_prime(primes, kxp)

        if kxp is None or p * p > limit:
            break

        ## find next primes and add them to primes list
        nix = None
        for (jx, cp) in enumerate(cprimes):
            if cp[0] % p == 0:   ## cp is a tuple
                cprimes[jx] = (cprimes[jx][0], False)
                nix = jx         ## Found first multiple
                break

        if nix is not None:
            for jx in range(nix, ncp, p):
                cprimes[jx] = (cprimes[jx][0], False)

        ## Add the first found primes to primes list
        while cix < len(cprimes) and cprimes[cix][0] <= p * p:
           cix = append_to(primes, cprimes, cix)

        if cix >= len(cprimes): break
    #
    ## last copy
    while cix < len(cprimes):
        cix = append_to(primes, cprimes, cix)

    return primes

def next_prime(primes, kx:int) -> Tuple[int, int]:
    if kx < len(primes):
        return (primes[kx], kx + 1)
    return (None, None)

def append_to(primes:List[int], cprimes:List[Tuple[int, int]], cix:int) -> int:
    if cprimes[cix][1]:
        primes.append(cprimes[cix][0])
    cix += 1
    return cix
