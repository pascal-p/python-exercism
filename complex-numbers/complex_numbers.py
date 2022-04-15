import math
from typing import Tuple


class ComplexNumber:
    pass  # Trick


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.re = real
        self.im = imaginary

    def __getattr__(self, attr):
        if attr == 'imaginary':
            return self.im
        elif attr == 'real':
            return self.re
        else:
            raise AttributeError(f"{attr} not implemented yet?")

    def __eq__(self, other: ComplexNumber) -> bool:
        return self.re == other.re and self.im == other.im

    def __add__(self, other: ComplexNumber) -> ComplexNumber:
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other: ComplexNumber) -> ComplexNumber:
        (a, b) = self.to_tuple()
        (c, d) = other.to_tuple()
        return ComplexNumber(a * c - b * d, b * c + a * d)

    def __sub__(self, other: ComplexNumber) -> ComplexNumber:
        return ComplexNumber(self.re - other.re, self.im - other.im)

    def __truediv__(self, other: ComplexNumber) -> ComplexNumber:
        (a, b) = self.to_tuple()
        (c, d) = other.to_tuple()
        den = c * c + d * d
        return ComplexNumber((a * c + b * d) / den,
                             (b * c - a * d) / den)

    def __abs__(self) -> ComplexNumber:
        return math.sqrt(self.re * self.re + self.im * self.im)

    def conjugate(self) -> ComplexNumber:
        return ComplexNumber(self.re, -self.im)

    def exp(self) -> ComplexNumber:
        a = math.exp(self.re)
        return ComplexNumber(a * math.cos(self.im), a * math.sin(self.im))

    def to_tuple(self) -> Tuple[float, float]:
        return (self.re, self.im)

    def __str__(self):
        # for end-user
        return f"{self.re} + {self.im}.i"

    def __repr__(self):
        # for dev
        # f"({self.re}, {self.im})"
        return f"{self.re} + {self.im}.i"
