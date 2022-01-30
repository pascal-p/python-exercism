import typing

EXPECTED_BAKE_TIME = 40 # min

PREPARATION_TIME = 2 # the time it takes to prepare a single layer (min)

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int - remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    diff = EXPECTED_BAKE_TIME - elapsed_bake_time
    return diff if diff > 0 else 0

def preparation_time_in_minutes(num_of_layers: int) -> int:
    """
    Implement the preparation_time_in_minutes() function that takes the number 
    of layers you want to add to the lasagna as an argument and 
    returns how many minutes you would spend making them. 
    Assume each layer takes 2 minutes to prepare.

    >>> preparation_time_in_minutes(2)
    4
    """
    return num_of_layers * PREPARATION_TIME if num_of_layers > 0 else 0

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """
    Implement the elapsed_time_in_minutes() function that has two parameters:
    :param number_of_layers (the number of layers added to the lasagna) and
    :param elapsed_bake_time (the number of minutes the lasagna has been baking in the oven).

    This function should return
    - the total number of minutes you've been cooking, or
    - the sum of your preparation time and the time the lasagna has already spent baking in the oven.
    :return: int - total number of minutes you've been cooking,

    >>> elapsed_time_in_minutes(3, 20)
    26
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
