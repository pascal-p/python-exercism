"""
    Aliens
"""

from typing import List, Tuple

HEALTH_LEVEL = 3


class Alien:
    total_aliens_created = 0

    def __init__(self, x: int, y: int):
        self.x_coordinate = x
        self.y_coordinate = y
        self.health = HEALTH_LEVEL
        self.__class__.total_aliens_created += 1

    def hit(self):
        """
        ```python
        >>> alien = Alien(0, 0)
        >>> alien.health
        3
        # Decrements health by 1 point.
        >>> alien.hit()
        >>> alien.health
        2
        ```
        """
        if self.health >= 0:
            self.health -= 1
            return self
        # TODO: raise when negative

    def is_alive(self):
        """
        ```python
        >>> alien.health
        1
        >>> alien.is_alive()
        True
        >>> alien.hit()
        >>> alien.health
        0
        >>> alien.is_alive()
        False
        ```
        """
        return self.health > 0

    def teleport(self, dx: int, dy: int):
        """
        ```python
        >>> alien.teleport(5, -4)
        >>> alien.x_coordinate
        5
        >>> alien.y_coordinate
        -4
        ```
        """
        self.x_coordinate += dx
        self.y_coordinate += dy
        return self

    def collision_detection(self, _other):
        pass


def new_aliens_collection(positions: List[Tuple[int, int]]) -> List[Alien]:
    """Function taking a list of position tuples, creating one Alien instance per position.

    :param positions: list - A list of tuples of (x, y) coordinates.
    :return: list - A list of Alien objects.
    """

    return [
        Alien(*pos) for pos in positions
    ]
