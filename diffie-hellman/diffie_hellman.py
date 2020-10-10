import random
import secrets
import math

def private_key(p):
    check_factor(p)
    return random.randint(3, p-1)

def public_key(p, g, private):
    check_key(private, p)
    return g ** private % p

def secret(p, public, private):
    check_key(private, p)
    check_key(public, p, tag='pubh')
    return public ** private % p

#
# use stronger randomness module with secrets
#

def s_private_key(p):
    check_factor(p)
    return secrets.choice(range(3, p))

def s_public_key(p, g, private):
    return public_key(p, g, private)

def s_secret(p, public, private):
    return secret(p, public, private)


#
# helpers
#

def check_factor(f):
    if f < 2 or not is_prime(f):
        raise ValueError("factor must be a prime number >= 2")

def check_key(pkey, p, tag='priv'):
    if pkey < 2 or pkey >= p:
        raise ValueError("not a valid key")


def is_prime(p: int) -> bool:
    if p % 2 == 0 and p > 2:
        return False # raise ArgumentError("not a prime number")

    sp = math.floor(math.sqrt(p))
    for d in range(3, sp, 2):
        if p % d == 0:
            return False
    return True
