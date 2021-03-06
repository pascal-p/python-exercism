from typing import Tuple
import re
import functools

# ADDITIONS
#  - validation number of rails <= len of message to enocde/decode
#  - if message contains blank delete/ignore them
#  - uppercase and remove all punctuation...

NON_LETTERS = re.compile(r'[^A-Z0-9]+')

## decorator
def check_arg(fn):
    @functools.wraps(fn)
    def wrapped_fn(*args, **kwargs):
        (message, rails) = args
        #
        if len(message) == 0: return message
        if rails == 1: return message
        if rails > len(message):
            return message
            # raise ValueError("rails (length) should be less than message's length to encode/decode")
        #
        args = [NON_LETTERS.sub('', message.upper()), rails, *args[2:]]
        return fn(*args, **kwargs)
    #
    return wrapped_fn

@check_arg
def encode(message: str, rails: int) -> str:
    r = fill(message, rails, defl='.')
    # print("==> r: ", r)
    ciphered = [
        ch for jx in range(rails) for ch in list(r[jx]) if ch != '.'
    ]
    # print("==> ciphered: ", ciphered)
    return ''.join(ciphered)

@check_arg
def decode(encoded_message: str, rails: int) -> str:
    msg_ph = '?' * len(encoded_message) # ''.join(['?'] * len(encoded_message))
    # 1 - Compute zig-zag with placeholder (ph)
    r = fill(msg_ph, rails, defl='.')
    #
    # 2 - fill place holder
    lix, ix = 0, 0
    for jx in range(rails):
        while ix < len(r[jx]):
            if r[jx][ix] == '?':
                r[jx][ix] = encoded_message[lix]
                lix += 1
            ix += 1
        ix = 0
    #
    # 3 - construct decoded message
    decoded = []
    # assume all r have same lengths and read column by column
    for ix in range(len(r[0])):
        for jx in range(rails):
            if r[jx][ix] != '.':
                decoded.append(r[jx][ix])
                break
    #
    return ''.join(decoded)

def fill(message: str, rails: int, defl='.'):
    r = [[] for _ in range(rails)]
    kx, incr = 0, True
    for l in list(message):
        for jx in range(rails):
            if incr:
                r[jx].append(l if kx == jx else defl)
            else:
                r[rails - 2 - jx].append(l if kx == rails - 2 - jx else defl)
        kx, incr = incr_fn(kx, incr, rails) if incr else decr_fn(kx, incr, rails)
    return r

def incr_fn(kx: int, incr: bool, rails: int) -> Tuple[int, bool]:
    kx = (kx + 1) % rails
    if kx == 0:
        kx = rails - 2
        incr = False
    return kx, incr

def decr_fn(kx: int, incr: bool, rails: int) -> Tuple[int, bool]:
    kx -= 1
    if kx == -1:
        kx = 1
        incr = True
    return kx, incr
