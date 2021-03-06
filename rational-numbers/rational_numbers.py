from __future__ import division
import functools

# using decorators and "private" helpers

def check_arg(fn):
    @functools.wraps(fn)
    def wrapper_fn(*args, **kwargs):
        # typically args will be 2 rationals (self and other)
        # we need tocheck validity of other (2nd arg)
        r = args[1]
        if r is None: raise ValueError('NaN')

        if type(r) is Rational:
            pass
        elif type(r) is int:
            r = Rational(r, 1)
        else:
            raise ValueError('NaN')

        res = fn(*[args[0], r, *args[2:]], **kwargs)
        # after: None
        return res

    return wrapper_fn


def _gcd(n, d):
    # n > 0 and d > 0
    n, d = (d, n) if n < d else (n, d)
    if d == 0: return n
    r = n
    while r > 1:
        r = n % d
        n, d = d, r
    return n if r == 0 else r

def _div_by_gvd(n, d):
    r = _gcd(n, d)
    return (n // r, d // r)

def _maker(numer, denom):
    if numer == denom:
        return (1, 1)

    sign = 1 if (numer >= 0 and denom >= 0) or (numer < 0 and  denom < 0) else -1
    numer, denom = abs(numer), abs(denom)
    numer, denom = _div_by_gvd(numer, denom)
    return (sign * numer, denom)

class Rational:
    """
    Integer overflow not taken into account!
    """
    def __init__(self, numer, denom):
        if denom == 0:
            raise ZeroDivisionError('Denominator cannot be 0')
        self.numer, self.denom = _maker(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    @check_arg
    def __add__(self, other):
        return Rational(self.numer * other.denom + self.denom * other.numer,
                        self.denom * other.denom)

    @check_arg
    def __sub__(self, other):
        return Rational(self.numer * other.denom - self.denom * other.numer,
                        self.denom * other.denom)
    @check_arg
    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    @check_arg
    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power is None or type(power) is not int:
            raise ValueError('NaN or Not an Integer')

        if self.numer == 0 and power == 0:
            raise ArithmeticError("0/n ** 0 is undefined")

        if power >= 0:
            return Rational(self.numer ** power, self.denom ** power);
        else:
            p = abs(power);
            return Rational(self.denom ** p, self.numer ** p);

    def __rpow__(self, base):
        """
        Ex. 9 ** Rational(-1, 2)
        """
        if base is None or \
           (type(base) is not int and type(base) is not float):
            raise ValueError('NaN')
        if (base == 0 or base == 0.0) and self.numer == 0:
            raise ArithmeticError("0 ** 0 is undefined")
        return base ** (self.numer / self.denom)
