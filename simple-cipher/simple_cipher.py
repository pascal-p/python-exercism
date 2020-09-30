from typing import Dict, Tuple
import functools, re
import secrets


def check_input(fn):
    @functools.wraps(fn)
    def wrapper_fn(*args, **kwargs):
        _, text = args # _ is self
        check = kwargs
        if check: Cipher._check(text)
        res = fn(*args, **kwargs)
        return res

    return wrapper_fn


class Cipher:
    _ALPHA = "abcdefghijklmnopqrstuvwxyz"
    LEN_ALPHA = len(_ALPHA)
    HSH     = { k: v for k, v in zip(list(_ALPHA), range(LEN_ALPHA)) }
    REV_HSH = { v: k for k, v in HSH.items() }

    def __init__(self, key=None):
        if key is None:
            key = ''.join([__class__.REV_HSH[secrets.randbelow(__class__.LEN_ALPHA)] for _ in range(100)])
        else:
            __class__._check(key)
            key = key.lower()
        self.key = key
        self.klen = len(key)

    @check_input
    def encode(self, text, check=True):
        return self._transcode(text, __class__._trans_fn)

    @check_input
    def decode(self, text, check=True):
        return self._transcode(text, __class__._rev_trans_fn)

    def _transcode(self, msg, fn):
        return ''.join(
            map(lambda tup: __class__.REV_HSH[fn(self, *tup)],
                filter(lambda tup: re.match(r'[a-z]', tup[1]),
                       enumerate(msg.lower()))
            )
        )

    @staticmethod
    def _check(inp):
        if not re.match(r'\A[a-z]+\Z', inp):
            raise ValueError('Expecting only Latin lower case characters')
        return

    @staticmethod
    def _rev_trans_fn(this, ix, ch):
        jx = __class__.HSH[ch] - __class__.HSH[this.key[ix % this.klen]]
        jx = __class__.LEN_ALPHA + jx if jx < 0 else jx
        return jx % __class__.LEN_ALPHA

    @staticmethod
    def _trans_fn(this, ix, ch):
        jx = __class__.HSH[ch] + __class__.HSH[this.key[ix % this.klen]]
        return jx % __class__.LEN_ALPHA
