#
# python3 takes care of overflow...
#

def square_of_sum(n: int) -> int:
    """
    Calculate Square the sum of the first `n` positive integers"

    Σ (1:n)² ≡ (n × (n + 1) / 2)²
    """
    x1 = n
    x2 = n + 1
    x3 = (x1 * x2) >> 1  # div by 2
    return x3 * x3


def sum_of_squares(n: int) -> int:
    """
    Sum the squares of the first `n` positive integers

    1² + 2² + 3² + ... + n² ≡ (n × (n + 1) × (2n + 1)) / 6
    """
    x1, x2, x3 = n, n + 1, (n << 1) + 1
    x4 = (x1 *  x2 * x3) >> 1
    return x4 // 3


def difference_of_squares(n: int) -> int:
    return square_of_sum(n) - sum_of_squares(n)
