def is_isogram(inp:str) -> bool:
    hsh = {}

    for l in inp.lower():
        if 'a' <= l <= 'z':
            hsh[l] = hsh.get(l, 0) + 1
    #
    # Note: we could also abort right after we detect a key with more than 1 value
    return len(list(
        filter(lambda kv_t: kv_t[1] > 1, hsh.items())
    )) == 0
