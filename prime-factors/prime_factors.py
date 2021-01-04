from typing import List
import math

PRIME_FACT_LT20 = [2, 3, 5, 7, 11, 13, 17, 19]

def factors(value: int) -> List[int]:
    if value <= 1: return []
    if value == 2: return [2]

    ## start with 2
    ix, cp = 0, 2  ## cp == candidate prime divisor
    factors = []
    primes = PRIME_FACT_LT20

    incr = 10 ** math.ceil(math.log(math.sqrt(value)) / math.log(10))

    while True:
        if value in primes:
            factors.append(value)
            break

        while value % cp == 0:
            value //= cp
            factors.append(cp)

        if value <= 1: break
        cp, ix, primes = next_prime(ix, cp + incr, primes)

    return factors

def next_prime(ix: int, limit: int, primes:List[int]) -> int:
    ix += 1
    if ix < len(primes):
        return (primes[ix], ix, primes)

    last_prime = primes[-1]
    not_a_prime = False

    for cv in range(last_prime + 2, limit, 2):
        for pr in primes[1:-1]:
            if cv % pr == 0:
                not_a_prime = True
                break ## not a prime

            if pr * pr > cv:
                primes.append(cv) ## found a prime
                break

        if not_a_prime:
            not_a_prime = False
            continue

    return (primes[ix], ix, primes)


# generator:
# if p < PRIME_FACT_LT20[-1]:
#    return (next(filter(lambda x: x > p, PRIME_FACT_LT20)), primes)
