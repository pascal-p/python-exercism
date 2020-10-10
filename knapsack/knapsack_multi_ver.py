import functools

# ======================================================================
# V1 - explicit enumeration (brute force)
# ======================================================================
#
def gen_all_subsets(s1):
    """
    s1 set of tuples
    """
    s1 = sorted(s1, key=lambda h: (h['weight'], h['value']))
    l2 = 2 ** len(s1)
    s2, nc = [ [] ], [ [] ]
    while len(s2) < l2:
        cs, nc = nc, []
        for c in cs:
            for e in s1:
                if e in c: continue
                ns = sorted(c + [e], key=lambda h: (h['weight'], h['value']))
                if ns not in nc: nc.append(ns)
                if ns not in s2: s2.append(ns)
    return s2

def drop_lt_capacity(items, c):
    return [item for item in items if sum([h['weight'] for h in item]) < c]

def find_max(items):
    def max_fn(tmax, item):
         s = sum([h['value'] for h in item])
         if s > tmax[0]:
             tmax = (s, item)
         return tmax
    return functools.reduce(max_fn, items, (-1, []))

def knapsack(items, c, show=False):
    nitems = gen_all_subsets(items)
    if show: print(f"1 - gen all subsets: {nitems}")
    nitems = drop_lt_capacity(nitems, c)
    if show: print(f"2 - drop those less than capacity {c}: {nitems}")
    return find_max(nitems)


knapsack([{'weight': 5, 'value':10}, {'weight':4, 'value': 40}, {'weight':4, 'value': 50}], 10)
# == (90, [{'weight': 4, 'value': 40}, {'weight': 4, 'value': 50}])

knapsack([{'weight': 5, 'value':15}, {'weight':4, 'value': 40}, {'weight':6, 'value': 30},
          {'weight':4, 'value': 50}, {'weight':5, 'value': 80}], 10)
# == (130, [{'weight': 4, 'value': 50}, {'weight': 5, 'value': 80}])


# ======================================================================
# V2 implicit enumeration, using recursivity
# ======================================================================
#

def get_val(sol):
    return sum([h['value'] for h in sol])

def k_rec_fn(items, c, n, sol):
    if n <= 0 or c <= 0: return sol
    if items[n - 1]['weight'] > c:
        return k_rec_fn(items, c, n - 1, sol)
    #
    sol1 = k_rec_fn(items, c - items[n - 1]['weight'], n - 1,     # sol. including n-th item
                    sol + [items[n - 1]])
    sol2 = k_rec_fn(items, c, n - 1,                       # sol. not including n-th item
                    sol)
    return sol1 if get_val(sol1) > get_val(sol2) else sol2 # cmp which sol. is better

def knapsack_rec(items, c):
    items = sorted(items, key=lambda h: (h['weight'], h['value'])) # primary
    sol = k_rec_fn(items, c, len(items), [])
    return get_val(sol), sol

knapsack_rec([{'weight': 5, 'value':10}, {'weight':4, 'value': 40}, {'weight':4, 'value': 50}], 10)
# == (90, [{'weight': 4, 'value': 50}, {'weight': 4, 'value': 40}])

knapsack_rec([{'weight': 5, 'value':15}, {'weight':4, 'value': 40}, {'weight':6, 'value': 30},
              {'weight':4, 'value': 50}, {'weight':5, 'value': 80}], 10)
# == (130, [{'weight': 5, 'value': 80}, {'weight': 4, 'value': 50}])

# ======================================================================
# V3 DP
# ======================================================================
def init_tables(n, c):
    table = [
        [-1] * (c + 1) for _ in range(n + 1)
    ]
    used_items = [
        [0] * (c + 1) for _ in range(n + 1)
    ]
    for ix in range(0, n + 1):
        table[ix][0] = 0
    for ix in range(1, c + 1):
        table[0][ix] = 0
    return table, used_items

def display_result(items, table, used_items, c):
    n = len(items)
    def first_row(ix):
        if ix == 0: print("              ", end='')
        else: print(f"{ix:2d} | ({items[ix - 1]['weight']}, {items[ix - 1]['value']}) |", end='')
        return
    #
    for ix in range(0, n + 1):
        first_row(ix)
        for cap in range(0, c + 1):
            print(f"{table[ix][cap]:3d}", end=' ')
        print()
    print()
    for ix in range(0, n + 1):
        first_row(ix)
        for cap in range(0, c + 1):
            print(f"{used_items[ix][cap]:3d}", end=' ')
        print()
    return

def find_items(items, used_items, c):
    n = len(items)
    ix, jx, sol = n, c, [] # start at (n, c) with []
    while ix > 0:
        if used_items[ix][jx] == 1:
            sol.append(items[ix - 1])
            ix, jx = ix - 1, jx - items[ix - 1]['weight']
        else:
            ix -= 1
    return sol

def knapsack_dp(items, c, show=False):
    """
    c == capacity or max_weight allowed

    use table(num_items + 1, capacity from 0 to c)
    keep track of which item(s) was/were used
    """
    n = len(items)
    table, used_items = init_tables(n, c)
    for ix in range(1, n + 1):
        for cap in range(1, c + 1):
            if items[ix - 1]['weight'] <= cap:
                # current weight is less than capacity, thus can be used
                rcap = cap - items[ix - 1]['weight']
                v1 = items[ix - 1]['value'] + table[ix - 1][rcap]
                v2 = table[ix - 1][cap]
                # now get max value by either using this weight or not
                if v1 > v2:
                    table[ix][cap] = v1
                    used_items[ix][cap] = 1
                else:
                    table[ix][cap] = v2
                #
            else:
                # ignore this itme then...
                table[ix][cap] = table[ix-1][cap]
    #
    if show:
        display_result(items, table, used_items, c)
        return table[n][c], find_items(items, used_items, c)
    return table[n][c]

knapsack_dp([{'weight': 5, 'value':10}, {'weight':4, 'value': 40}, {'weight':4, 'value': 50}], 10, show=True)

 #              0   0   0   0   0   0   0   0   0   0   0
 # 1 | (5, 10) |  0   0   0   0   0  10  10  10  10  10  10
 # 2 | (4, 40) |  0   0   0   0  40  40  40  40  40  50  50
 # 3 | (4, 50) |  0   0   0   0  50  50  50  50  90  90  90

 #                0   0   0   0   0   0   0   0   0   0   0
 # 1 | (5, 10) |  0   0   0   0   0   1   1   1   1   1   1
 # 2 | (4, 40) |  0   0   0   0   1   1   1   1   1   1   1
 # 3 | (4, 50) |  0   0   0   0   1   1   1   1   1   1   1

# (90, [{'weight': 4, 'value': 50}, {'weight': 4, 'value': 40}])

knapsack_dp([{'weight': 5, 'value':15}, {'weight':4, 'value': 40}, {'weight':6, 'value': 30},
             {'weight':4, 'value': 50}, {'weight':5, 'value': 80}], 10, show=True)
#                 0   0   0   0   0   0   0   0   0   0   0
#  1 | (5, 15) |  0   0   0   0   0  15  15  15  15  15  15
#  2 | (4, 40) |  0   0   0   0  40  40  40  40  40  55  55
#  3 | (6, 30) |  0   0   0   0  40  40  40  40  40  55  70
#  4 | (4, 50) |  0   0   0   0  50  50  50  50  90  90  90
#  5 | (5, 80) |  0   0   0   0  50  80  80  80  90 130 130

#                 0   0   0   0   0   0   0   0   0   0   0
#  1 | (5, 15) |  0   0   0   0   0   1   1   1   1   1   1
#  2 | (4, 40) |  0   0   0   0   1   1   1   1   1   1   1
#  3 | (6, 30) |  0   0   0   0   0   0   0   0   0   0   1
#  4 | (4, 50) |  0   0   0   0   1   1   1   1   1   1   1
#  5 | (5, 80) |  0   0   0   0   0   1   1   1   0   1   1
# (130, [{'weight': 5, 'value': 80}, {'weight': 4, 'value': 50}])
