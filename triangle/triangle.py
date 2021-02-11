from typing import Union, Tuple

IF = Union[int, float]

def equilateral(sides: Tuple[IF]):
    try:
        t = Triangle(*sides)
        return t.equilateral()

    except ValueError:
        return False

def isosceles(sides: Tuple[IF]):
    try:
        t = Triangle(*sides)
        return t.isosceles()

    except ValueError:
        return False

def scalene(sides: Tuple[IF]):
    try:
        t = Triangle(*sides)
        return t.scalene()

    except ValueError:
        return False

class Triangle:
    def __init__(self, x: IF, y: IF, z: IF):
        if x > 0 and y > 0 and z > 0 and \
           __class__.is_triangle((x, y, z)):
            self.x = x
            self.y = y
            self.z = z
        else:
            raise ValueError("Not a triangle")

    def equilateral(self):
        return self.x == self.y == self.z

    def isosceles(self):
        return any(
            map(lambda t: t[0] == t[1],
                __class__.all_pairs((self.x, self.y, self.z)))
        )

    def scalene(self):
        return all(
            map(lambda t: t[0] != t[1],
                __class__.all_pairs((self.x, self.y, self.z)))
        )

    @staticmethod
    def all_pairs(t):
        assert len(t) >= 3
        return [(t[ix], t[jx]) for ix in range(len(t)) for jx in range(ix+1, len(t)) if ix < jx]

    @staticmethod
    def is_triangle(t):
        (x, y, z) = t
        if z == max(t):
            return z <= x + y
        elif y == max(t):
            return y <= x + z
        else:
            return x <= y + z
