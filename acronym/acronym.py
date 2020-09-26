import re

def abbreviate(words: str) -> str:
    if len(words) == 0: return ""

    first_letter = lambda w: w[0].upper() if 'a' <= w[0].lower() <= 'z' \
        else w[1].upper()

    return ''.join(map(first_letter,
                       filter(lambda s: s != '',
                              re.split(r'[\s,\.:;\-_"]', words))))
