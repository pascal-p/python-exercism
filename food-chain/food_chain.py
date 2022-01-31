
ANIMALS = [
    '', 'fly', 'spider', 'bird', 'cat', 'dog', 'goat', 'cow', 'horse'
]

TEMPLATES = {
    1:  'I know an old lady who swallowed a ',
    -1: "I don't know why she swallowed the fly. Perhaps she'll die.",
    2: ' that wriggled and jiggled and tickled inside her.',
    3: 'She swallowed the ',
    4: ' to catch the ',
    5: 'She swallowed the <s1> to catch the <s2>',
}

SPEC = {
    1: '',
    2: 'It wriggled and jiggled and tickled inside her.',
    3: 'How absurd to swallow a <s>!',
    4: 'Imagine that, to swallow a <s>!',
    5: 'What a hog, to swallow a <s>!',
    6: 'Just opened her throat and swallowed a <s>!',
    7: "I don't know how she swallowed a <s>!",
    8: "She's dead, of course!",
}


def recite(start_verse: int, end_verse: int) -> list[str]:
    assert 1 <= start_verse <= end_verse, \
        f"Expecting start_verse({start_verse}) < end_verse({end_verse})"
    poem = []
    for ix in range(start_verse, end_verse + 1):
        poem = [*poem, *strophe(ix), '']
    return poem[:-1]


def strophe(start_v: int):
    a_strophe = [TEMPLATES[1] + ANIMALS[start_v] + "."]

    if start_v == 8:
        a_strophe.append(SPEC[8])
        return a_strophe

    if start_v >= 2:
        a_strophe.append(SPEC[start_v].replace('<s>', ANIMALS[start_v]))

    if start_v >= 4:
        for ix in range(start_v, 3, -1):
            a_strophe.append(TEMPLATES[3] + ANIMALS[ix] +
                             TEMPLATES[4] + ANIMALS[ix - 1] + '.')

    if start_v >= 3:
        # "She swallowed the " <bird> " to catch the " <spider> " that wriggled
        # and jiggled and tickled inside her.",
        a_strophe.append(TEMPLATES[3] + ANIMALS[3] +
                         TEMPLATES[4] + ANIMALS[2] + TEMPLATES[2])

    if start_v >= 2:
        a_strophe.append(
            TEMPLATES[5].replace('<s1>', ANIMALS[2]).replace(
                "<s2>", ANIMALS[1]) + '.'
        )
    #
    # end strophe
    a_strophe.append(TEMPLATES[-1])
    # print(f"for start_v {start_v} => ", a_strophe)
    # return '\n'.join(a_strophe)
    return a_strophe
