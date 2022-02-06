"""
   Tisbury Treasure Hunt
"""

from typing import Tuple, Union


def get_coordinate(record: Tuple) -> str:
    """

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.

    ```python
    >>> get_coordinate(("Scrimshaw Whale's Tooth", "2A"))
    "2A"
    ```
    """

    return record[1]


def convert_coordinate(coordinate: str) -> Tuple:
    """

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate seperated into its individual
            components.

    ```python
    >>> convert_coordinate("2A")
    ("2", "A")
    ```
    """

    return tuple(c for c in coordinate)


def compare_records(azara_record: Tuple, rui_record: Tuple) -> bool:
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.

    ```python
    >>> compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue'))
    False

    >>> compare_records(('Model Ship in Large Bottle', '8A'),
    ('Harbor Managers Office', ('8', 'A'), 'purple'))
    True
    ```
    """

    return convert_coordinate(get_coordinate(azara_record)) == rui_record[1]


def create_record(azara_record: Tuple, rui_record: Tuple) -> Union[Tuple, str]:
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.

    ```python
    >>> create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse',
    ('4', 'B'), 'Blue'))
    ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')

    >>> create_record(('Brass Spyglass', '4B'), (('1', 'C'), 'Seaside Cottages',
    'blue'))
    "not a match"
    ```
    """

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    else:
        return "not a match"


def clean_up(combined_record_group: Tuple[Tuple]) -> str:
    """

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned".
            Excess coordinates and information removed.

    ```python
    >>> clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'),
    'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)',
    ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'),
    'Purple')))

    "
    ('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')\n
    ('Vintage Pirate Hat', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')\n
    ('Crystal Crab', 'Old Schooner', ('6', 'A'), 'Purple')\n
    "
    ```
    """

    return '\n'.join(
        [str((*tuple[0:1], *tuple[2:])) for tuple in combined_record_group]
    ) + '\n'
