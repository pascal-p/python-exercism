import functools

def decode(string: str) -> str:
    if len(string) == 0: return ''

    def fn(l, x):
        """
        l contains the decoded string so far and optionally
        the multiplicator (integer), so ['xyxyayyx'] or ['xyxyayyx', 2]
        """
        is_digit = lambda x: x >= '0' and x <= '9'
        is_last_digit = is_digit(l[-1])

        if is_digit(x):
            if is_last_digit:
                l[-1] += x
            else:
                l.append(x)
        else:
            l[0] += x * int(l.pop(-1)) if is_last_digit else x

        return l

    ary = functools.reduce(fn,
                           list(string),
                           [''])
    return ary[0]

def encode(string: str) -> str:
    if len(string) == 0: return ''
    #
    def fn(l, x):
        if x in l[-1]:
            l[-1][1] += 1
        else:
            l.append([x, 1])
        return l
    #
    ary = functools.reduce(fn,
                           list(string),
                           [['', 0]])
    print(ary)
    return ''.join([str(n) + s if n > 1 else s for (s, n) in ary if n > 0])
