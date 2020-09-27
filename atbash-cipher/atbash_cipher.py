import re, functools

GROUP_FACT = 5 + 1  # counting 1 extra space

def encode(plain_text: str, enc=True) -> str:
    def trans_fn(s: str, ch: str) -> str:
        if not re.search(r'[a-zA-Z0-9]+', ch): return s

        s = s + ch if '0' <= ch <= '9' else \
            s + chr(ord('z') - ord(ch.lower()) + ord('a'))

        return s + ' ' if enc and len(s) % GROUP_FACT == 0 else s

    return functools.reduce(
        trans_fn,    # lambda s, ch: trans_fn(s, ch),
        plain_text,  # enumerate letters
        ' ').strip(' ')

def decode(ciphered_text:str) -> str:
    return encode(ciphered_text, enc=False)
