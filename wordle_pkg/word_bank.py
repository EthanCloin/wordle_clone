import random

from pyparsing import Word


class WordleLetter:
    CORRECT = 1
    WRONG = 0
    PARTIAL = -1
    CORRECTNESS_VALUES = [CORRECT, WRONG, PARTIAL]

    def __init__(self, letter):
        """constructor"""
        self._letter = letter
        self._correctness = None

    def __eq__(self, other):
        """ensure that letter is the comparison factor for this class"""
        if self.letter == other.letter:
            return True
        return False

    def set_correctness(self, correctness_value):
        """setter for correctness attribute

        Args:
            correctness_value (int): one of three constants defined by class

        Returns:
            bool: True if accepted value, otherwise False
        """

        if correctness_value in self.CORRECTNESS_VALUES:
            self.correctness = correctness_value
            return True
        return False

    def get_correctness(self):
        return self._correctness


def generate_word():
    """return a random word from the defined list of 10
    Eventually should refactor to use some kind of Dictionary.com API

    Returns:
        str: 5 letter word from internal list
    """
    valid_words = ["crane", "power", 'slice', 'flier', 'eerie',
                   "drape", "slime", "brain", "plead", "gnarl"]

    return random.choice(valid_words)


def validate_guess(previous_guesses, cur_guess):
    """checks that a guess is a 5 letter alpha str

    Args:
        previous_guesses (list): words already present on the board
        cur_guess (str): word to be validated

    Returns:
        bool: True if valid, otherwise False
    """
    if len(cur_guess) == 5 and cur_guess.isalpha():
        # check whether already guessed
        if cur_guess not in previous_guesses:
            return True
        else:
            print("You already guessed that!")
    else:
        print("5 letter words ONLY!")

    return False


def score_word(user_guess, solution_word):
    """use enumerate to check for matches on the correct index?"""
    pass
    # wordle_word = []
    # for letter in user_guess:
    #     wordle_letter = WordleLetter(letter)
    #     if letter in solution_word:
