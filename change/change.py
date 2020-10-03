import sys


def find_fewest_coins(coins, target):
    """
    Correctly determine the fewest number of coins to be given to a customer such
    that the sum of the coins' value would equal the correct amount of change.

    Using DP technique.
    res_ary is an array of array: [number of coins, [array of change]]
    """
    if target < 0:
        raise ValueError("Negative totals are not allowed.")
    res_ary = [[sys.maxsize, []] for _ in range(target+1)]
    res_ary[0][0] = 0
    #
    for t in range(1, target+1):
        for c in filter(lambda c: t - c >= 0, coins):
            n, ch = res_ary[t - c]
            if n != sys.maxsize and n + 1 < res_ary[t][0]:
                res_ary[t] = [n + 1, [c, *ch]]
    ## check
    if sum(res_ary[target][1]) != target:
        raise ValueError(f'The total {target} cannot be represented in the given currency.')
    return res_ary[target][1]


def find_fewest_coins_rec(coins, target):
    """
    Working but exponential...
    Returning only the number of coins...
    """
    if target < 0: raise ValueError("Negative totals are not allowed.")
    if target == 0: return 0
    #
    res_min = sys.maxsize
    for c in filter(lambda c: target - c >= 0, coins):
        n = find_fewest_coins_rec(coins, target - c)
        if n + 1 < res_min: res_min = n + 1
    if res_min == 0 or res_min == sys.maxsize:
        raise ValueError(f'The total {target} cannot be represented in the given currency.')
    return res_min
