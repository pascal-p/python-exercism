"""
   Making the Grade
"""

from typing import List


def round_scores(student_scores: List[float]) -> List[int]:
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.

    ```python
    >>> student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
    >>> round_scores(student_scores)
    ...
    [40, 39, 95, 80, 25, 31, 70, 55, 40, 90]
    ```
    """

    return [
        round(m) for m in student_scores
    ]


def count_failed_students(student_scores: List[int]) -> int:
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.

    ```python
    >>> count_failed_students(student_scores=[90, 40, 55, 70, 30, 25,
    80, 95, 38, 40])
    5
    ```
    """

    return sum(
        [0 if n > 40 else 1 for n in student_scores]
    )


def above_threshold(student_scores: List[int], threshold: int) -> List[int]:
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.

    ```python
    >>> above_threshold(student_scores=[90, 40, 55, 70, 30, 68, 70, 75, 83, 96],
    threshold=75)
    [90, 75, 83, 96]
    ```
    """

    return [
        n for n in student_scores if n >= threshold
    ]


def letter_grades(highest: int) -> List[int]:
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade
             interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100

    ```python
    >>> letter_grades(highest=100)
    [41, 56, 71, 86]

    ```
    """

    step = (highest - 40) // 4
    return [n for n in range(41, highest, step)]


def student_ranking(student_scores: List[int], student_names: List[str]) -> List[str]:
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].

    ```python
    >>> student_scores = [100, 99, 90, 84, 66, 53, 47]
    >>> student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']
    >>> student_ranking(student_scores, student_names)
    ...
    ['1. Joci: 100', '2. Sara: 99', '3. Kora: 90', '4. Jan: 84', '5. John: 66', '6. Bern: 53', '7. Fred: 47']
    ```
    """

    return [
        f"{ix + 1}. {name}: {score}" for (ix, (score, name)) in
        enumerate(zip(student_scores, student_names))
    ]


def perfect_score(student_info: List[List]) -> List:
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100
    is found.

    ```python
    >>> perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]])
    ["Alex", 100]

    >>> perfect_score(student_info=[["Charles", 90], ["Tony", 80]])
    []
    ```
    """

    for student_name, score in student_info:
        if score == 100:
            return [student_name, score]
    return []
