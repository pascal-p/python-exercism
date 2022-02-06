"""
   Card Games
"""

from typing import List

def get_rounds(number: int) -> List[int]:
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.

    ```python
    >>> get_rounds(27)
    [27, 28, 29]
    ```
    """

    return [n for n in range(number, number + 3)]


def concatenate_rounds(rounds_1: List[int], rounds_2: List[int]) -> List[int]:
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.

    ```python
    >>> concatenate_rounds([27, 28, 29], [35, 36])
    [27, 28, 29, 35, 36]
    ```
    """

    return [
        *rounds_1, *rounds_2
    ]


def list_contains_round(rounds: List[int], number: int) -> bool:
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?

    ```python
    >>> list_contains_round([27, 28, 29, 35, 36], 29)
    True

    >>> list_contains_round([27, 28, 29, 35, 36], 30)
    False
    ```
    """

    return number in rounds


def card_average(hand: List[int]) -> float:
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    assert len(hand) > 0
    return sum(hand) / len(hand)


def approx_average_is_average(hand: List[int]) -> bool:
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.

    ```python
    >>> approx_average_is_average([1, 2, 3])
    True

    >>> approx_average_is_average([2, 3, 4, 8, 8])
    True

    >>> approx_average_is_average([1, 2, 3, 5, 9])
    False
    ```
    """

    assert len(hand) % 2 == 1
    r_avg = card_average(hand)
    a_avg1 = (hand[0] + hand[-1]) / 2
    a_avg2 = hand[len(hand) // 2]
    return a_avg1 == r_avg or a_avg2 == r_avg


def average_even_is_average_odd(hand: List[int]) -> bool:
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?

    ```python
    >>> average_even_is_average_odd([1, 2, 3])
    True

    >>> average_even_is_average_odd([1, 2, 3, 4])
    False
    ```
    """

    ary_even, ary_odd = [0, *hand][::2], hand[::2]
    avg_even = sum(ary_even) / (len(ary_even) - 1)
    avg_odd = sum(ary_odd) / len(ary_odd)
    return avg_even == avg_odd


def maybe_double_last(hand: List[int]) -> list[int]:
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.

    ```python
    >>> hand = [5, 9, 11]
    >>> maybe_double_last(hand)
    [5, 9, 22]

    >>> hand = [5, 9, 10]
    >>> maybe_double_last(hand)
    [5, 9, 10]
    ```
    """

    return hand if hand[-1] != 11 else [*hand[:-1], 22]
