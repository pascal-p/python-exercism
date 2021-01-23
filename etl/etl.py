from typing import Dict, List


def transform(legacy_data: Dict[int, List[str]]) -> Dict[str, int]:
    return {
        l.lower(): ix for (ix, lst) in legacy_data.items() \
        for l in lst
    }
