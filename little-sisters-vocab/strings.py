"""
   Little Sister's Vocabulary
"""

def add_prefix_un(word: str) -> str:
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.

    ```python
    >>> add_prefix_un("happy")
    'unhappy'

    >>> add_prefix_un("manageable")
    'unmanageable'
    ```
    """

    return 'un' + word 


def make_word_groups(vocab_words: list[str]) -> str:
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.

    ```python
    >>> make_word_groups(['en', 'close', 'joy', 'lighten'])
    'en :: enclose :: enjoy :: enlighten'

    >>> make_word_groups(['pre', 'serve', 'dispose', 'position'])
    'pre :: preserve :: predispose :: preposition'

    >> make_word_groups(['auto', 'didactic', 'graph', 'mate'])
    'auto :: autodidactic :: autograph :: automate'

    >>> make_word_groups(['inter', 'twine', 'connected', 'dependent'])
    'inter :: intertwine :: interconnected :: interdependent'
     ```
    """

    pre = vocab_words[0]
    sep = ' :: '
    return pre + sep + sep.join(
        [pre + word for word in vocab_words[1:]]
    )


def remove_suffix_ness(word: str) -> str:
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.

    ```python
    >>> remove_suffix_ness("heaviness")
    'heavy'

    >>> remove_suffix_ness("sadness")
    'sad'
    ```
    """
    new_word = word.replace('ness', '')
    return new_word.replace('i', 'y') if new_word.endswith('i') else new_word


def adjective_to_verb(sentence: str, index: int) -> str:
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.

    ```python
    >>> adjective_to_verb('I need to make that bright.', -1 )
    'brighten'

    >>> adjective_to_verb('It got dark as the sun set.', 2)
    'darken'
    ```
    """

    assert 0 <= index < len(sentence) or -len(sentence) < index <= 0, f"index {index} out of range"
    words = sentence.split()
    adj_at = words[index]
    if adj_at[-1].lower() not in char_range('a', 'z'):
        adj_at = adj_at[0:-1]
    return adj_at + 'en'

# Helper 
def char_range(c1: str, c2: str):
    """Generates the characters from `c1` to `c2`, inclusive."""

    return [chr(ix) for ix in range(ord(c1), ord(c2)+1)]
