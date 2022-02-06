"""
   Chaitana's Colossal Coaster
"""

from typing import List

def add_me_to_the_queue(express_queue: List, normal_queue: List, ticket_type: int,
                        person_name: str) -> List:
    """

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue:  list - names in the normal queue.
    :param ticket_type:  int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.

    ```python
    >>> add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=1, person_name="RichieRich")
    ...
    ["Tony", "Bruce", "RichieRich"]

    >>> add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=0, person_name="HawkEye")
    ....
    ["RobotGuy", "WW", "HawkEye"]
    ```
    """

    assert 0 <= ticket_type <= 1
    if ticket_type == 0:
        # with mutation
        normal_queue.append(person_name)
        return normal_queue # [*normal_queue, person_name]
    else:
       express_queue.append(person_name)
       return express_queue # [*express_queue, person_name]


def find_my_friend(queue: List, friend_name: str) -> int:
    """

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.

    ```python
    >>> find_my_friend(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], friend_name="Steve")
    ...
    1
    ```
    """

    assert friend_name in queue
    # assuming case is fine (no need to normalize)
    return queue.index(friend_name)


def add_me_with_my_friends(queue: List, index: int, person_name: str) -> List:
    """

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.

    ```python
    >>> add_me_with_my_friends(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], index=1, person_name="Bucky")
    ...
    ["Natasha", "Bucky", "Steve", "T'challa", "Wanda", "Rocket"]
    ```
    """

    assert 0 <= index <= len(queue) or -len(queue) - 1 <= index <= -1
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: List, person_name: str) -> List:
    """

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return:  list - queue update with the mean persons name removed.

    ```python
    >>> remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran")
    ...
    ["Natasha", "Steve", "Wanda", "Rocket"]
    ```
    """

    queue.remove(person_name)
    return queue
    
    


def how_many_namefellows(queue: List, person_name: str) -> int:
    """

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return:  int - the number of times the name appears in the queue.

    ```python
    >>> how_many_namefellows(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha")
    ...
    2
    ```
    """

    return len(
        [ix for ix, p in enumerate(queue) if p == person_name]
    )


def remove_the_last_person(queue: List) -> List:
    """

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.

    ```python
    >>> remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
    ...
    'Rocket'
    ```
    """

    return queue.pop()


def sorted_names(queue: List) -> List:
    """

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.

    ```python
    >>> sorted_names(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
    ...
    ['Eltran', 'Natasha', 'Natasha', 'Rocket', 'Steve']
    ```
    """
    
    return sorted(queue)
