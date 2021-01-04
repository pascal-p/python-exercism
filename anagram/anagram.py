from typing import List
# python 3.8

def find_anagrams(word:str, candidates:List[str]) -> bool:
    cw = transform(word)
    cword = word.lower()
    al = []
    for c in candidates:
        if len(word) != len(c) or cword == c.lower():
            continue
        if transform(c) == cw:
            al.append(c)
    return al

def transform(w:str) -> str:
    return ''.join(
        sorted([l for l in w.lower()])
    )

def otransform(w:str) -> str:
    lw = [l for l in w.lower()]
    lw.sort() # in place
    return ''.join(lw)
