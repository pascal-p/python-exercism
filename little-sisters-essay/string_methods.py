"""
   Little Sister's Essay
"""

from typing import List

def capitalize_title(title: str) -> str:
    """

    :param title: str title string that needs title casing
    :return:  str title string in title case (first letters capitalized)

    ```python
    >>> capitalize_title("my hobbies")
    "My Hobbies"
    ```
    """

    return " ".join(
        [word.capitalize() for word in title.split()]
    )

def check_sentence_ending(sentence):
    """

    :param sentence: str a sentence to check.
    :return:  bool True if punctuated correctly with period, False otherwise.

    ```python
    >>> check_sentence_ending("I like to hike, bake, and read.")
    True
    ```
    """

    assert len(sentence) > 0
    return sentence[-1].endswith('.')


def clean_up_spacing(sentence: str) -> str:
    """

    :param sentence: str a sentence to clean of leading and trailing space characters.
    :return: str a sentence that has been cleaned of leading and trailing space characters.

    ```python
    >>> clean_up_spacing(" I like to go on hikes with my dog.  ")
    "I like to go on hikes with my dog."
    ```
    """

    return " ".join(
        [w for w in sentence.split()]
    )


def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
    """

    :param sentence: str a sentence to replace words in.
    :param old_word: str word to replace
    :param new_word: str replacement word
    :return:  str input sentence with new words in place of old words

    ```python
    >>> replace_word_choice("I bake good cakes.", "good", "amazing")
    "I bake amazing cakes."
    ```
    """

    return sentence.replace(old_word, new_word)
