import re

def translate(text: str) -> str:
    return ' '.join(
        list(
            map(lambda w: _translate(w),
                re.split(r"\s+", text))
        )
    )

def _translate(word: str) -> str:
    if re.match(r"\A[aeiou]|\A(?:sr|yt)", word, re.I):
        # starting with a vowel sound
        return word + 'ay'

    elif re.match(r"\Ay[aeiou]", word, re.I):
        return re.sub(r"\A(y)(.*)\Z", "\g<2>\g<1>ay", word)

    elif re.match(r"\A(thr|sch)[aeiou]", word, re.I):
        return re.sub(r"\A(.{3})(.*)\Z", "\g<2>\g<1>ay", word)

    elif re.match(r"\A[sy]qu|^(ch|qu|th)", word, re.I):
        return re.sub(r"\A(.qu|ch|qu|th)(.*)\Z", "\g<2>\g<1>ay", word)

    elif re.match(r"\A(p|r|s|t)hy", word, re.I):
        return re.sub(r"\A(.h)(y.*)\Z", "\g<2>\g<1>ay", word)

    elif re.match(r"\Amy\Z", word, re.I):
        return re.sub(r"\A(m)(y.*)\Z", "\g<2>\g<1>ay", word)

    elif re.match(r"\Axr", word, re.I):
        return word + 'ay'

    elif re.match(r"\A[bcdfghjklmnpqrstvwxyz]", word, re.I):
        # starting with a consonnant sound
        return re.sub(r"\A(.)(.*)\Z", "\g<2>\g<1>ay", word)

    else:
        raise NotImplementedError("Case not yet implemented")

    return ""
