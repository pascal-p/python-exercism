import re
import functools

REXP = r'[\s\d\.\-_,;:\'"\(|\)\[|\]]'
ALL_LETTERS = {'a', 'b', 'c', 'd', 'e', 'f' , 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

def is_pangram_v1(sentence: str) -> str:
    "build a hash (dict) of letters "
    if len(sentence) == 0: return False

    def hsh_fn(hsh, x):
        hsh[x] = 1 if x not in hsh else hsh[x] + 1
        return hsh

    hsh = functools.reduce(hsh_fn,
                           filter(lambda x: not re.match(REXP, x),
                                  list(sentence.lower())),
                           {})

    letters = list(hsh.keys())
    return sorted(letters) == sorted(ALL_LETTERS)

def is_pangram(sentence: str) -> str:
    "build a set from beginning"
    if len(sentence) == 0: return False

    def set_fn(s, x):
        s.add(x)
        return s

    _set = functools.reduce(set_fn,
                            filter(lambda x: not re.match(REXP, x),
                                   list(sentence.lower())),
                            set())
    return _set == ALL_LETTERS
