import math, re

def largest_product(series, size):
    """"
    Adjacent places...

    scan the series by sliding a window of size: length

    - if any 0 in that window keep moving to exclude the zero...
    - if only 9 in the window - stop early
    - what else?
    """
    if series == '' and size == 0:
        return 1

    if not re.match(r'\A[0-9]+\Z', series) or \
       size < 0 or \
       len(series) < size:
        raise ValueError("Expect a non empty numerical string as input")
    #
    max_s, max_seq = 0, []
    for ix in range(len(series) - size + 1):
        seq = series[ix:ix + size]
        if '0' in seq: continue
        s = math.prod(map(lambda s: int(s), seq), start=1)
                          # series[ix:ix + size]), start=1)
        #
        if s > max_s:
            max_s = s
            max_seq = seq
            if re.match(r"\A9+\Z", max_seq): break
    #
    return (max_s, max_seq)[0]
