from typing import List, Any

def append(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    add all elements for list2 at the end of list1

    do not use append or extend...
    do not modify list1
    """
    if length(list1) == 0: return list2
    if length(list2) == 0: return list1

    # return [*list1, *list2] # using splat operator
    return list1 + list2


def concat(lists: List[List[Any]]) -> List[Any]:
    if length(lists) <= 1:
        return lists

    (nl, *rl) = lists
    for l in rl:
        if length(l) == 0: continue
        nl += l

    return nl


def filter(function, list: List[Any]) -> List[Any]:
    """
    return elements of list that satisfy (predicate) function
    """
    if length(list) == 0: return list

    return [x for x in list if function(x)]


def length(list: List[Any]) -> int:
    n = 0
    for _x in list: n += 1
    return n


def map(function, list: List[Any]) -> List[Any]:
    if length(list) == 0: return list

    return [function(x) for x in list]


def foldl(function, list: List[Any], initial: Any) -> Any:
    if length(list) == 0: return initial
    #
    acc = initial
    for x in list:
        acc = function(acc, x)

    return acc


def foldr(function, list: List[Any], initial: Any) -> Any:
    if length(list) == 0: return initial

    acc = initial
    for x in list[::-1]:
        acc = function(x, acc)

    return acc


def reverse(list: List[Any]) -> List[Any]:
    if length(list) == 0: return list

    # list[::-1]
    nl = []
    for x in list:
        nl = [x] + nl

    return nl


def any(function, list: List[Any]) -> bool:
    if length(list) == 0: return True

    for x in list:
        if function(x): return True
    return False


def all(function, list: List[Any]) -> bool:
    if length(list) == 0: return True

    for x in list:
        if not function(x): return False
    return True
