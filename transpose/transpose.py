from typing import List
import re

PAD = chr(0)

def transpose(lines:List) -> List:
    if len(lines) == 0: return lines

    maxlen = max(map(lambda s: len(s), lines))

    ## pad if necessary
    nlines = map(lambda s: pad(s, maxlen), lines)

    ## combine
    res = [[*args] for args in zip(*nlines)]

    ## stringify
    nres = map(lambda a: ''.join(a), res)

     ## suppress the added PAD at the end (right)
    nres = map(lambda s: re.sub(rf"{PAD}+\Z", '', s), nres)

    ## replace remaining left PAD with space
    nres = map(lambda s: re.sub(rf"{PAD}", ' ', s), nres)
    return list(nres)

def pad(s:str, nlen:int) -> List:
    clen = len(s)
    l = list(s)
    for _ in range((nlen - clen)):
        l.append(PAD)
    return l
