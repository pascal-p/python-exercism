YA_MAP = {
    1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
    6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
    50: 'L', 100: 'C', 500: 'D', 1000: 'M'
}

LIMITS = (1, 3000)

def roman(number: int) -> str:
    if type(number) is not int:
        raise TypeError("Not an Integer!")

    if number < LIMITS[0] or number > LIMITS[1]:
        raise ValueError('Outside validity interval')

    if number in YA_MAP: return YA_MAP[number]

    roman, p = '', 1000
    while True:
        num, rem = (number // p, number % p)

        if num > 0:
            if p == 1_000:
                roman += YA_MAP[p] * num
            elif p == 100 or p == 10:
                roman = roman_helper(roman, num, p)
            else:
                ## p == 1
                roman += YA_MAP[num]

        if rem == 0: break
        number, p = rem, p // 10

    return roman

def roman_helper(roman: str, num: int, p: int) -> str:
    if num <= 3:
        args = (YA_MAP[p] * num,)                      # ex. 30 => XXX

    elif num == 4:
        args = (YA_MAP[p], YA_MAP[5 * p])              # ex. 40 => XL

    elif num < 9:
        args = (YA_MAP[5 * p], YA_MAP[p] * (num - 5))  # ex. 70 => LXX

    else:
        args = (YA_MAP[p], YA_MAP[10 * p])             # ex. 90 => XC

    return roman + ''.join(args)
