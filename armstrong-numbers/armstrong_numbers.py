import functools

def is_armstrong_number(number:int) -> bool:
    """
    Caveat: possible integer overflow...
    """
    n = len(str(number))
    return functools.reduce(lambda s, d: s + int(d)**n, str(number), 0) == number
