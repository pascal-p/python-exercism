def classify(n:int) -> str:
    check_domain(n)
    s = sum_proper_div(n)

    if is_perfect(n, s):
        return "perfect"

    elif is_abundant(n, s):
        return "abundant"

    else:
        return "deficient"

def sum_proper_div(n:int) -> int:
    d, s = 2, 1
    while d * d <= n:
        m, r = divmod(n, d)
        if r == 0:
            s += d if m == d else d + m
        d += 1
    return s

def is_abundant(n:int, s:int) -> bool:
    return s > n

def is_perfect(n:int, s:int) -> bool:
    if n == 1: return False
    return s == n

def is_deficient(n:int, s:int) -> bool:
    if n == 1: return True
    return s < n

def check_domain(n:int):
    if n <= 0:
        raise(ValueError("Expecting a strictly positive integer"))
    return
