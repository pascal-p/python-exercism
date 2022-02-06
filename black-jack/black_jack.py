"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

from typing import Union, Tuple

CARD_VAL = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10,
    'A': 1
}

def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.

    ```python
    >>> value_of_card('K')
    10

    >>> value_of_card('4')
    4

    >>> value_of_card('A')
    1
    ```
    """
    
    assert card in list(CARD_VAL.keys())
    return CARD_VAL[card]


def higher_card(card_one: str, card_two: str) -> Union[str, Tuple[str, str]]: 
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.

    ```python
    >>> higher_card('K', '10')
    ('K', '10')

    >>> higher_card('4', '6')
    '6'

    >>> higher_card('K', 'A')
    'K'
    ```
    """

    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    elif value_of_card(card_two) > value_of_card(card_one):
        return card_two
    return (card_one, card_two)

def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10;
           'A' = 11 (if already in hand); numerical value otherwise.

    :return: int - value of the upcoming ace card (either 1 or 11).

    ```python
    >>> value_of_ace('6', `K`)
    1

    >>> value_of_ace('7', '3')
    11
    ```
    """

    if card_one == 'A' or card_two == 'A':
        return 1
    s = value_of_card(card_one) + value_of_card(card_two) + 11
    return 11 if s <= 21 else 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).

    ```python
    >>> is_blackjack('A', 'K')
    True

    >>> is_blackjack('10', '9')
    False
    ```
    """
    return (card_one == 'A' and card_two in ('10', 'K', "Q", 'J')) or \
        (card_two == 'A' and card_one in ('10', 'K', "Q", 'J'))


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).

    ```python
    >>> can_split_pairs('Q', 'K')
    True

    >>> can_split_pairs('10', 'A')
    False
    ```
    """

    return value_of_card(card_one) == value_of_card(card_two)
 

def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).

    ```python
    >>> can_double_down('A', '9')
    True

    >>> can_double_down('10', '2')
    False
    ```
    """

    return value_of_card(card_one) + value_of_card(card_two) in (9, 10, 11)
