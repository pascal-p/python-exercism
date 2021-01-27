GIFTS = [
    ("first", "a Partridge in a Pear Tree"),
    ("second", "two Turtle Doves"),
    ("third", "three French Hens"),
    ("fourth", "four Calling Birds"),
    ("fifth", "five Gold Rings"),
    ("sixth", "six Geese-a-Laying"),
    ("seventh", "seven Swans-a-Swimming"),
    ("eighth",  "eight Maids-a-Milking"),
    ("ninth", "nine Ladies Dancing"),
    ("tenth", "ten Lords-a-Leaping"),
    ("eleventh", "eleven Pipers Piping"),
    ("twelfth", "twelve Drummers Drumming")
]

OPENING = "On the <n> day of Christmas my true love gave to me: "

def recite(start_verse: int, end_verse: int):
    assert start_verse >= 1 and end_verse <= len(GIFTS)

    if start_verse == end_verse:
        return single_suite(start_verse, end_verse)

    return [
        single_suite(ix, ix)[0] for ix in range(start_verse, end_verse + 1)
    ]

def single_suite(start_verse: int, end_verse: int):
    (day, gift) = GIFTS[end_verse - 1]
    verses = [
        OPENING.replace("<n>", day),
        f"{gift}, "
    ] + [
        f"{GIFTS[ix][1]}, " for ix in range(end_verse - 2, -1, -1)
    ]

    verses[-1] = verses[-1].replace(", ", ".")
    if len(verses) > 2:
        verses[-1] = verses[-1].replace("a Partridge", "and a Partridge")

    return ["".join(verses)]
