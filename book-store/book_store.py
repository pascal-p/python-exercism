#
# Next using memoizing and dynamic programming...
#
def total(basket, promo={2: 5, 3: 10, 4: 20, 5: 25}, cost=800):

    def _total(basket):
        n = len(basket)

        if n == 0: return ([], 0)
        if n == 1:
            return ([], cost)

        ## copies of same book?
        same_cpy, count = same_copies(basket)
        if same_cpy:
            return ([], count * cost)

        ## only 1 copy?
        if n < 6 and  all_diff(basket):
            return ([], n * cost * (1 - promo[n] / 100))

        ## now grouping is possible
        min_cost = n * (cost + 100) # value greater than the possible max.

        for g in promo.keys():
            gp, rbasket = pick_from(basket, g)
            k = len(gp)
            if k == 0: break
            cost_gp = k * cost * (1 - promo[k] / 100)
            rbasket, cost_ = _total(rbasket)
            min_cost = min(min_cost, cost_gp + cost_)

        return (basket, min_cost)
    #
    # let's re-order the basket
    book_cnt = count_book_cpy(basket)
    nbasket = []
    ## re-order key by number of value decreasing
    ## ex. [1, 1, 2, 3, 4, 4, 5, 5]  =>  [1, 1, 4, 4, 5, 5, 2, 3]
    for k in sorted(book_cnt, key=lambda k: book_cnt[k], reverse=True):
        nbasket += [*[k] * book_cnt[k]]
    _, res = _total(nbasket)
    return int(res)

def count_book_cpy(basket):
    book_cnt = {}
    for bc in basket:
        book_cnt[bc] = book_cnt.get(bc, 0) +1
    return book_cnt

def same_copies(basket):
    book_cnt = count_book_cpy(basket)
    if len(book_cnt.keys()) == 1:
        key = list(book_cnt.keys())[0]
        return (True, book_cnt[key])
    return (False, 0)

def all_diff(basket):
    book_cnt = count_book_cpy(basket)
    for k in book_cnt.keys():
        if book_cnt[k] > 1: return False
    return True

def pick_from(basket, n):
    m, cbasket = len(basket), [*basket] # make a copy
    if n > m or n > len(set(basket)):
        return ([], basket)
    # raise ValueError(f"Cannot pick {n} item(s) from list of {m} item(s)")

    pick, k = [], 0
    for item in cbasket:
        if item not in pick:
            pick.append(item)
            k += 1
        if k == n: break
    #
    assert len(set(pick)) == n, f"pick {pick} should be of len: {n}"
    #
    # now remove item in pick from basket
    for item in pick: cbasket.remove(item)
    return (pick, cbasket)
