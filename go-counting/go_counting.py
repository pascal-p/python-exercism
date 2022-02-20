"""
    Go counting
"""

from typing import Tuple, Set, Dict, List


BLACK = 'B'   # black
WHITE = 'W'   # white
NONE = ' '

# flake8: noqa: E501


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = [*board]         # make a copy of the board
        self.y_limit = len(self.board)
        self.x_limit = len(self.board[0])

    def territory(self, x: int, y: int) -> Tuple[str, Set]:
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.

        To be more precise an empty intersection is part of a player's territory
        if all of its neighbors are either stones of that player or empty
        intersections that are part of that player's territory.
        """
        if not(0 <= x < self.x_limit) or not(0 <= y < self.y_limit):
            raise ValueError('Invalid coordinate')
        if self.board[y][x] != NONE:
            return (NONE, set())
        neighbors = self.get_neighbors(x, y)
        if len(neighbors) == 0:
            return (NONE, set(((0, 0), )))
        count = self.get_color_partition(neighbors)
        if count[WHITE] == 0 and count[NONE] == 0:  # all black
            return (BLACK, set(((x, y), )))
        elif count[BLACK] == 0 and count[NONE] == 0:  # all white
            return (WHITE, set(((x, y), )))
        #
        return self.get_territory(neighbors)

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        res = {BLACK: set(), WHITE: set(), NONE: set()}
        s = set(
            [(x, y) for x in range(0, self.x_limit)
             for y in range(0, self.y_limit)]
        )
        while len(s) > 0:
            (x, y) = s.pop()
            color, territory = self.territory(x, y)
            res[color] |= territory  # union
            s -= territory
        return res

    def get_neighbors(self, x: int, y: int):
        """
        determine the neighbors (horizontal and vertical only) of a given cell
        """
        return list(
            filter(
                lambda t: (0 <= t[0] < self.x_limit) and (
                    0 <= t[1] < self.y_limit),
                [
                    (x - 1, y),
                    (x + 1, y),
                    (x, y - 1),
                    (x, y + 1)
                ]
            )
        )

    def get_color_partition(self, neighbors: List[Tuple[int, int]]) -> Dict[str, int]:
        """
        given the neighbors of a cell, count how many are Black, White  and None
        """
        res = {WHITE: 0, BLACK: 0, NONE: 0}
        for (x, y) in neighbors:
            res[self.board[y][x]] += 1
        return res

    def get_territory(self, neighbors: List[Tuple[int, int]]):
        done, territory, color = [], [], ''
        while len(neighbors) > 0:
            (x, y) = neighbors[0]
            xy_color = self.board[y][x]
            if color == '':
                if xy_color != NONE:
                    color = xy_color
            elif color == WHITE and xy_color == BLACK:
                color = NONE
            elif color == BLACK and xy_color == WHITE:
                color = NONE
            if xy_color in (BLACK, WHITE):
                neighbors = [*neighbors[1:]]
                done.append((x, y))
            else:
                c_neighbors = [
                    (x_, y_) for (x_, y_) in self.get_neighbors(x, y)
                    if (x_, y_) not in neighbors and (x_, y_) not in done
                ]
                territory.append((x, y))
                done.append((x, y))
                neighbors = [*neighbors[1:], *c_neighbors]
            #
        if color == '':
            color = NONE
        return (color, set(territory))
