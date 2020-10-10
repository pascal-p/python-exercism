def maximum_value(max_weight, items, show=False):
    n, c = len(items), max_weight
    table, used_items = init_tables(n, c)
    for ix in range(1, n + 1):
        for cap in range(1, c + 1):
            if items[ix - 1]['weight'] > cap:
                # ignore this itme then...
                table[ix][cap] = table[ix-1][cap]
                continue
            #
            # otherwise current weight is less than capacity, thus can be used
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
    if show:
        display_result(items, table, used_items, c)
        return table[n][c], find_items(items, used_items, c)
    return table[n][c]

def init_tables(n, c):
    """
    - n numbers of items
    - c max_weight
    """
    table = [
        [-1] * (c + 1) for _ in range(n + 1)
    ]
    used_items = [
        [0] * (c + 1) for _ in range(n + 1)
    ]
    for ix in range(0, n + 1): table[ix][0] = 0
    for ix in range(1, c + 1): table[0][ix] = 0
    return table, used_items

def display_result(items, table, used_items, c):
    n = len(items)
    def first_row(ix):
        if ix == 0: print("              ", end='')
        else:
            print(f"{ix:2d} | ({items[ix - 1]['weight']}, {items[ix - 1]['value']}) |", end='')
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
