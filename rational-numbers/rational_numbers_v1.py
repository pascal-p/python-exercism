from __future__ import division


class Rational:
    """
    Integer overflow not taken into account!
    """
    def __init__(self, numer, denom):
        if denom == 0:
            raise ZeroDivisionError('Denominator cannot be 0')
        if numer == denom:
            numer, denom = 1, 1
        sign = 1 if (numer >= 0 and denom >= 0) or (numer < 0 and  denom < 0) else -1
        numer, denom = abs(numer), abs(denom)
        numer, denom = __class__._div_by_gvd(numer, denom)
        self.numer, self.denom = sign * numer, denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        other = __class__._check_arg(other)
        return Rational(self.numer * other.denom + self.denom * other.numer,
                        self.denom * other.denom)

    def __sub__(self, other):
        other = __class__._check_arg(other)
        return Rational(self.numer * other.denom - self.denom * other.numer,
                        self.denom * other.denom)

    def __mul__(self, other):
        other = __class__._check_arg(other)
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        other = __class__._check_arg(other)
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
        if base is None or \
           (type(base) is not int and type(base) is not float):
            raise ValueError('NaN')
        if (base == 0 or base == 0.0) and self.numer == 0:
            raise ArithmeticError("0 ** 0 is undefined")
        return base ** (self.numer / self.denom)

    @staticmethod
    def _gcd(n, d):
        # n > 0 and d > 0
        n, d = (d, n) if n < d else (n, d)
        if d == 0: return n
        r = n
        while r > 1:
            r = n % d
            n, d = d, r
        return n if r == 0 else r

    @staticmethod
    def _div_by_gvd(n, d):
        r = __class__._gcd(n, d)
        return (n // r, d // r)

    @staticmethod
    def _check_arg(r):
        if r is None: raise ValueError('NaN')

        if type(r) is Rational:
            return r

        if type(r) is int:
            return Rational(r, 1)

        raise ValueError('NaN')
