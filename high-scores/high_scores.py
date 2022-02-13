"""
   High Scores
"""

import functools
from typing import List


def check_scores(fn):  # decorator
    @functools.wraps(fn)
    def wrapped_fn(*args, **kwargs):
        (scores,) = args
        if len(scores) == 0:
            raise Exception('scores must not be empty')
        return fn(*args, **kwargs)
    return wrapped_fn


@check_scores
def latest(scores: List[int]) -> int:
    """
       returns latest recorded score in scores list
    """
    return scores[-1]


@check_scores
def personal_best(scores: List[int]) -> int:
    """
       returns bast (max.) from scores list
    """
    return max(scores)


@check_scores
def personal_top_three(scores: List[int]) -> List[int]:
    """
       returns top 3 scores from given list
    """
    return sorted(scores, reverse=True)[0:3]
