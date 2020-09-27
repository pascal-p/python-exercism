import re, functools

Punctuation = ','.join(['\'', ':', ';', '?', '!', ',', '.'])

def count_words(sentence: str) -> str:
    def update_fn(wc, w):
        wc[w] = wc[w] + 1 if w in wc else 1
        return wc

    def process(wc, w):
        "using walrus operator"
        if re.search(r"\A[\w']+\Z", w):
            wc = update_fn(wc, w)
        else:
            pattern = r"\A[^\w]*([\w']+)[^\w]*\Z"
            if (m := re.match(pattern, w)) and m is not None and m[1] != "'":
                wc = update_fn(wc, m[1])
        return wc

    ary = re.split(r"\t|\n|\s|,|_", sentence)
    ary = map(lambda w: w.strip(Punctuation), ary)
    ary = map(lambda w: w.lower(), ary)

    return functools.reduce(process, ary, {})
