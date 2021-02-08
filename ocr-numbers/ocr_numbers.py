from typing import Dict, List

DIGIT_MAP: Dict[int, List[str]] = {
    0: [" _ ", "| |", "|_|", "   "],
    1: ["   ", "  |", "  |", "   "],
    2: [" _ ", " _|", "|_ ", "   "],
    3: [" _ ", " _|", " _|", "   "],
    4: ["   ", "|_|", "  |", "   "],
    5: [" _ ", "|_ ", " _|", "   "],
    6: [" _ ", "|_ ", "|_|", "   "],
    7: [" _ ", "  |", "  |", "   "],
    8: [" _ ", "|_|", "|_|", "   "],
    9: [" _ ", "|_|", " _|", "   "],
}

N, M = (4, 3)

def convert(vstr: List[str]) -> str:
    if len(vstr) % N != 0:
        raise ValueError(f"input should be of length n, where n is a multiple of {N}, got {len(vstr)}")

    if all(map(lambda s: len(s) % M != 0, vstr)):
        raise ValueError(f"rows of input should be of length n, where n is a multiple of {M}")

    if len(vstr) == N and all(map(lambda s: len(s) == M, vstr)):
        return lookup(vstr)

    shape = (len(vstr), len(vstr[0]))
    r_s = ""

    for r in range(0, shape[0] - N + 1, N):
        for c in range(0, shape[1] - M + 1, M):
            r_s += lookup(
                [vstr[rix][c:c + M] for rix in range(r, r + N)]
            )

        r_s += ","
    #
    return r_s[0:-1]

def lookup(vstr: List[str]) -> str:
    for (k, v) in DIGIT_MAP.items():
        if vstr == v: return str(k)
    #
    return "?"
