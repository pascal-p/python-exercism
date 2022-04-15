import functools


def rebase(ibase, digits, obase):
    if ibase < 2:
        raise ValueError('input base must be >= 2')

    if obase < 2:
        raise ValueError('output base must be >= 2')

    # if len(digits) == 0: raise ValueError('Expect at least 1 digit')

    if len(list(filter(lambda x: x < 0 or x >= ibase, digits))) > 0:
        raise ValueError(f'all digits must satisfy 0 <= d < input base')

    n = tobase_10(ibase, digits)
    if obase == 10:
        return list(map(lambda s: int(s), list(str(n))))
    else:
        return from_10_to_obase(obase, n)


def tobase_10(ibase, digits):
    return functools.reduce(lambda n, d: n * ibase + d,
                            digits,
                            0)


def from_10_to_obase(obase, num):
    if num == 0:
        return [0]
    digits = []
    while num > 0:
        num, d = (num // obase, num % obase)
        digits.append(d)
    return digits[::-1]
