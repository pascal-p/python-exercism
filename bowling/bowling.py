"""
   Bowling
"""

from typing import List


class BowlingGame:
    NUM_FRAMES = 10
    MAX_PINS_VALUE = 10

    def __init__(self):
        self.pins = []
        self.pair = []

    def roll(self, pins: int):
        """
        records the pins and organize them as pairs
        """

        if pins > self.__class__.MAX_PINS_VALUE or pins < 0:
            raise ValueError("pins cannot be more than 10 or less than 0")

        if len(self.pins) == self.__class__.NUM_FRAMES:
            if len(self.pair) == 1:
                if self.is_spare(*self.pins[-1]):
                    raise ValueError("cannot roll more")
                if self.pair[0] < self.__class__.NUM_FRAMES and pins == self.__class__.MAX_PINS_VALUE:
                    raise ValueError("current pins cannot be a strike")
            else:
                # pair is empty, last frame is not a strike nor a spare => no fill
                if sum(self.pins[-1]) == 0:
                    raise ValueError("cannot roll more")

        if len(self.pins) == 11 and sum(self.pins[-1]) < self.__class__.MAX_PINS_VALUE:
            raise ValueError("cannot roll more")

        if pins == self.__class__.MAX_PINS_VALUE:
            self.pins.append((pins, 0))
            self.pair = []
        else:
            if len(self.pair) == 1:
                if self.pair[0] + pins > self.__class__.MAX_PINS_VALUE:
                    raise ValueError("two rolls cannot be > 10")
                self.pair.append(pins)
                self.pins.append(tuple(self.pair))
                self.pair = []
            elif len(self.pair) == 0:
                self.pair.append(pins)

    def score(self):
        if len(self.pair) == 1:
            self.pins.append((self.pair[0], 0))

        if len(self.pins) == self.__class__.NUM_FRAMES + 1 and self.is_strike(*self.pins[-1]) and \
                self.is_strike(*self.pins[-2]):
            raise ValueError(
                "cannot determine score as 10th, 11th frame were strikes")
        npins, score = self.pins, 0
        if len(npins) == self.__class__.NUM_FRAMES:
            if sum(npins[-1]) == self.__class__.MAX_PINS_VALUE:
                # last roll (pair) is a strike or spare - need bonus to calc score
                raise ValueError("Missing bonus rolls")
            score = self._calc_score(npins)
        elif len(npins) > self.__class__.NUM_FRAMES:
            if self.is_spare(*npins[-2]) or self.is_strike(*npins[-2]):
                score = self._calc_score(npins)
            else:
                raise ValueError("not a valid game - too much rolls")
        else:
            raise ValueError("not a valid game - not enough rolls")
        return score

    def is_strike(self, x: int, y: int) -> bool:
        return (x == 0 and y == self.__class__.MAX_PINS_VALUE) or (x == self.__class__.MAX_PINS_VALUE and y == 0)

    def is_spare(self, x: int, y: int) -> bool:
        return x > 0 and y > 0 and x + y == self.__class__.MAX_PINS_VALUE

    # def _normalize(self):
    #     npins = []
    #     pins = [*self.pins]
    #     for x in pins:
    #         if x == 10:
    #             npins.append(x)
    #             npins.append(0)  # insert a zero
    #         else:
    #             npins.append(x)
    #     if len(npins) % 2 == 1:
    #         npins.append(0)
    #     assert len(
    #         npins) % 2 == 0, f"expecting length of npins to be even, got {npins} / {len(npins)}"
    #     return [
    #         (x, y) for (x, y) in zip(npins[::2], [0, *npins][::2][1:])
    #     ]

    def _calc_score(self, pins):
        score = []
        curr = 0
        stack = ['foo']  # sentinelle
        for ix, (x, y) in enumerate(pins):
            if x == 0 and y == 0:
                score.append(0)
                continue
            curr = x + y
            if x + y < self.__class__.MAX_PINS_VALUE:
                stack.append('open')
            elif self.is_strike(x, y):
                curr = self.__class__.MAX_PINS_VALUE
                stack.append('strike')
            else:
                curr = self.__class__.MAX_PINS_VALUE
                stack.append('spare')

            if stack[-2] == 'open':
                pass
            elif stack[-2] == 'spare':
                score[-1] += x
            elif stack[-2] == 'strike':
                if x != 10:
                    score[-1] += x + y
                    if len(score) > 1 and stack[-3] == 'strike':
                        score[-2] += x
                else:
                    score[-1] += x
                    if len(score) > 1 and stack[-3] == 'strike':
                        score[-2] += x
            else:
                # sentinelle
                pass
            score.append(curr)
        stack = []
        return sum(score[:self.__class__.NUM_FRAMES])
