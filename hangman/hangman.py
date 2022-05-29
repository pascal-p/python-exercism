# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'
REMAINING_GUESS = 9


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = REMAINING_GUESS
        self.status = STATUS_ONGOING
        self._word = word.lower()
        self._masked_word = "_" * len(word)
        self._guessed_letters = set()

    def guess(self, char):
        char = char.lower()
        if self.remaining_guesses < 0 or self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")
        if self.remaining_guesses == 0:
            self.status = STATUS_LOSE
            # will keep going as we can win on the last guess
        #
        ixes = self._update_masked_word(char) if char not in self._guessed_letters \
            else []
        if len(ixes) == 0:
            self.remaining_guesses -= 1
        self._guessed_letters.add(char)
        return

    def get_masked_word(self):
        return self._masked_word

    def get_status(self):
        return self.status

    #
    # Private helpers
    #
    def _findall(self, char):
        return [
            ix for ix, ch in enumerate(self._word) if ch == char
        ]

    def _update_masked_word(self, char):
        ixes = self._findall(char)
        for ix in ixes:
            mw = self._masked_word
            self._masked_word = "".join([
                mw[0:ix], char, mw[ix+1:]
            ])
        if self._masked_word == self._word:
            self.status = STATUS_WIN
        return ixes
