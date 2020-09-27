import functools

Punctuation = ['\'', ',', '.', '?', '!', '"', ';', ':']

Digit_As_Char = list(map(lambda x: str(x), range(0, 10)))
Ord_a, Ord_A = (ord('a'), ord('A'))

def rot_n_maker(n: int):
    def rot_n(letter: str) -> str:
        if 'a' <= letter <= 'z':
            return chr(Ord_a + (ord(letter) - Ord_a + n) % 26)

        elif 'A' <= letter <= 'Z':
            return chr(Ord_A + (ord(letter) - Ord_A + n) % 26)

        elif letter in [' ', *Punctuation, *Digit_As_Char]:
            return letter

        else:
            raise Exception(f'{letter} is not in latin alphabet')
    return rot_n

def rotate(text: str, key: int) -> str:
    rot_n = rot_n_maker(key)

    return functools.reduce(
        lambda cipher, l: cipher + rot_n(l),
        text,
        ""
    )
