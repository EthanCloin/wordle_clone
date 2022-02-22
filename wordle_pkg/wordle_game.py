import word_bank
import console_ui


class WordleGame:
    def __init__(self):
        self.is_active = True
        self.guesses = []
        self.solution = word_bank.generate_word()
        self.latest_guess = []  # list of WordleLetters

    def add_guess(self, validated_guess):
        """append guess to guesses list"""
        self.guesses.append(validated_guess)

    def draw_board(self):
        """use console_ui to print board"""
        console_ui.print_console_board(self.guesses)

    def check_guess(self, guess):
        """determine whether each letter in the guess is correct, partial, or incorrect"""
        pass


class WordleLetter:
    CORRECT = 1
    WRONG = 0
    PARTIAL = -1
    CORRECTNESS_VALUES = [CORRECT, WRONG, PARTIAL]

    def __init__(self, letter, correctness=None):
        """constructor"""
        self._letter = letter
        self._correctness = correctness

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
