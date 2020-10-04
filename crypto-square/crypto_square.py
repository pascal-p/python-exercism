import re, math, functools
from typing import Tuple, List

def cipher_text(plain_txt:str, sep=' ') -> str:
    """
    cipher_text("If man was meant to stay on the ground, nature would have given us roots.")

    == 'imtgtdes fearuhn  mayorau  anouevs  ntnnwer  wttdogo  aohnuio  ssealvt '
    """
    if len(plain_txt) == 0: return ""

    norm_txt, n = normalize_src(plain_txt)
    r, c = square_coeff(n)

    chunks = segment_txt(norm_txt, c, r, n, sep=sep)

    return cipher_txt(chunks, c, sep=sep)

def normalize_src(plain_txt:str) -> str:
    norm_txt = re.sub(r"[^a-z0-9]+", '', plain_txt.lower())
    n = len(norm_txt)
    return (norm_txt, n)

def square_coeff(n: int) -> Tuple[int, int]:
    r = math.floor((1. + math.sqrt(1 + n * 4)) / 2.)
    c = r if r * r >= n else r + 1
    assert c * r >= n
    return (r, c)

def segment_txt(norm_txt:str, c:int, r:int, n:int, sep=' ') -> List[str]:
    chunks = [norm_txt[ix:min(ix + r, n) + 1] \
              for ix in range(0, n, c)]

    # pad last chunk if required
    if len(sep) > 0:
        llc = len(chunks[-1])
        chunks[-1] = chunks[-1] + sep * (c - llc)
    return chunks

def cipher_txt(chunks:List[str], c:int, sep=' ') -> str:
    return ' '.join([functools.reduce(lambda str, s: str + s[ix], chunks, "") \
                     for ix in range(0, c)])
