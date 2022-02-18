"""
    Inventory Exo
"""

from typing import List, Dict, Tuple


def create_inventory(items: List[str]) -> Dict[str, int]:
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    inventory = {}
    for k in items:
        if k in inventory:
            inventory[k] += 1
        else:
            inventory[k] = 1
    return inventory


def add_items(inventory: Dict[str, int], items: List[str]) -> Dict[str, int]:
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    for k in items:
        if k in inventory:
            inventory[k] += 1
        else:
            inventory[k] = 1
    return inventory


def decrement_items(inventory: Dict[str, int], items: List[str]) -> Dict[str, int]:
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for k in items:
        if k in inventory:
            if inventory[k] > 0:
                inventory[k] -= 1
        else:
            pass  # ignore k
    return inventory


def remove_item(inventory: Dict[str, int], item: List[str]) -> Dict[str, int]:
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """

    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory: Dict[str, int]) -> List[Tuple[str, int]]:
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    return [
        (k, v) for k, v in inventory.items() if v > 0
    ]
