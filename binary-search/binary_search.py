from typing import List, Any

"""
  1st approach
  search_list is sorted in asc. order + no duplicate
"""
def find(search_list:List[Any], value: Any, throw=True) -> int:
    if len(search_list) == 0:
        raise ValueError("Emtpy search list")

    ## edge cases
    if value < search_list[0] or value > search_list[-1]:
        return not_found(throw)

    # general case:
    l, h = 0, len(search_list) - 1
    while  l <= h:
        m = (l + h) // 2

        if value == search_list[m]:
            return m
        elif value < search_list[m]:
            h = m - 1
        else:
            l = m + 1
    return not_found(throw)

def not_found(throw):
    if throw:
        raise ValueError("Not found")
    else:
        return 0
