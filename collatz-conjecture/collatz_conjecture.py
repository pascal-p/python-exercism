def steps(n: int) -> int:
    if n < 1:
        raise ValueError("argument should be > 1")

    step = 0
    while n != 1:
        # Hopefully the conjecture is True - otherwise infinite loop!
        if n % 2 == 0:
            n //= 2
        else:            
            n = 3 * n + 1 # odd
        step += 1

    assert n == 1
    return step
