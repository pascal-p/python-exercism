"""
  Currency Exchnage Exo
"""

import typing

FACTOR = 100.0


def exchange_money(budget: float, exchange_rate: float) -> float:
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    res = int((budget / exchange_rate) * FACTOR)
    return res / FACTOR


def get_change(budget: float, exchanging_value: int) -> float:
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return int((budget - exchanging_value) * FACTOR) / FACTOR


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    assert denomination > 0 and number_of_bills > 0, \
        "Expecting denomination and number_of_bills to be > 0"
    return int(denomination * number_of_bills)


def get_number_of_bills(budget: float, denomination: int) -> int:
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    return int(budget) // denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int,
                       denomination: int) -> int:
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    return exch_value_helper(budget, exchange_rate, spread,
                             denomination)[1]


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """

    raw, exc_val = exch_value_helper(budget, exchange_rate, spread,
                                     denomination)
    return int(raw) - exc_val


def exch_value_helper(budget: float, exchange_rate: float, spread: int,
                      denomination: int) -> tuple[float, int]:
    """

    Internal helper function
    """

    spreadf = spread / FACTOR
    # applying spread to echange rate
    exc_rate_spread = exchange_rate * (1.0 + spreadf)
    res = budget / exc_rate_spread
    return (res, int(res / denomination) * denomination)
