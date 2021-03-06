from . import console_ui
from . import word_bank
from . import graphical_ui as gui
from enum import Enum


class WordleLetter:
    """represents a letter tile. class defines valid letters, correctness values, and comparison between instances
    """
    CORRECT = 1
    WRONG = 0
    PARTIAL = -1
    CORRECTNESS_VALUES = [CORRECT, WRONG, PARTIAL, None]
    ACCEPTED_LETTERS = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, letter: str, position: int, correctness=None):
        """constructor"""
        self._letter = self.letter_setter(letter)
        self.position = position
        self._correctness = correctness

    def __eq__(self, other):
        """ensure that letter is the comparison factor for this class"""
        return self.letter == other.letter

    @property
    def correctness(self):
        """_summary_

        Returns:
            int: correctness value
        """
        return self._correctness

    @correctness.setter
    def set_correctness(self, correctness_value):
        """setter for correctness attribute

        Args:
            correctness_value (int): one of three constants defined by class or None
        """

        if correctness_value not in self.CORRECTNESS_VALUES:
            raise ValueError
        self._correctness = correctness_value

    @property
    def letter(self):
        """getter for letter"""
        return self._letter

    def letter_setter(self, letter):
        """weird custom setter since constructor doesn't call actual property setters"""
        lower_letter = letter.lower()
        if lower_letter not in self.ACCEPTED_LETTERS:
            raise ValueError("only accepts alpha characters")
        return lower_letter


class WordleWord():
    """contains 5 wordle letters"""
    ACCEPTED_LEN = 5

    def __init__(self, letters: str):
        self.letters = WordleWord.to_wordle(letters)

    @staticmethod
    def to_wordle(letters: str) -> list[WordleLetter]:
        """converts string to list of WordleLetters"""

        if len(letters) != WordleWord.ACCEPTED_LEN:
            return None
        if not letters.isalpha():
            return None

        wl_list = []
        for idx, letter in enumerate(letters):
            wl_list.append(WordleLetter(letter, idx))
        return wl_list

    def check_against_solution(self, solution) -> bool:
        """compare a WordleWord guess to provided solution and update the correctness values"""
        if type(solution) is not WordleWord:  # possible spot for error
            solution = self.to_wordle(solution)

        # set correctness values for wordle letters
        for idx, letter in enumerate(self.letters):
            if letter in solution:
                if letter.position == solution[idx].position:
                    letter.correctness = WordleLetter.CORRECT
                letter.correctness == WordleLetter.PARTIAL
            letter.correctness == WordleLetter.WRONG

        # check for exact match
        for letter in self.letters:
            if letter.correctness != WordleLetter.CORRECT:
                return False

        return True


class WordleGame:
    """represents the game as a whole. contains methods to draw the board, validate guesses, 
    and check for victory condition
    """

    MAX_GUESSES = 6

    # Status constants
    class Status(Enum):
        LOSE = 0
        WIN = 1
        IN_PROGRESS = -1

    def __init__(self, solution: WordleWord):
        self.is_active = True
        self.guesses = []  # list of WordleWords
        self.solution = solution

    # NEEDS REFACTORED TO GUI
    def draw_board(self) -> None:
        console_ui.print_console_board(self.guesses)

    def accept_input(self) -> None:
        """loops until valid guess, then adds valid guess to guesses"""

        guess = None
        while not guess:
            input_str = input(">> ")
            guess = WordleWord.to_wordle(input_str)

        self.guesses.append(guess)

    # def validate_guess(self, user_guess: str) -> bool:
    #     """checks that a guess is a 5 letter alpha str

    #     Args:
    #         previous_guesses (list): words already present on the board
    #         cur_guess (str): word to be validated

    #     Returns:
    #         bool: True if valid, otherwise False
    #     """

    #     if len(user_guess) == 5 and user_guess.isalpha():
    #         # check whether already guessed
    #         if user_guess not in self.guesses_list:
    #             self.add_guess(user_guess)
    #             return True
    #         print("You already guessed that!")
    #     print("5 letter words ONLY!")

    #     return False

    # def process_valid_guess(self) -> None:
    #     """compares a given guess and solution to generate a list of WordleLetter instances
    #     which have appropriate correctness values

    #     Args:
    #         user_guess (str): valid word guessed by user
    #         solution_word (str): correct word

    #     """

    #     # clear latest_guess and update list of guessed words
    #     self.latest_guess_letters.clear()
    #     latest_guess = self.guesses_list[len(self.guesses_list) - 1]
    #     print(f"latest guess is: {latest_guess}")

    #     for idx, letter in enumerate(latest_guess):
    #         # check for perfect match
    #         if letter == self.solution[idx]:
    #             # add WL object with CORRECT value to list
    #             self.latest_guess_letters.append(
    #                 WordleLetter(letter, WordleLetter.CORRECT))
    #         elif letter in self.solution:
    #             self.latest_guess_letters.append(
    #                 WordleLetter(letter, WordleLetter.PARTIAL))
    #         else:
    #             self.latest_guess_letters.append(
    #                 WordleLetter(letter, WordleLetter.WRONG))

    def check_solution(self) -> bool:
        """checks whether the latest guess is totally correct

        Returns:
            bool: _description_
        """

        # if any letter in last guess isn't correct, return false
        for letter in self.guesses[-1]:
            if letter.correctness != WordleLetter.CORRECT:
                return False
        return True

    def check_game_over(self) -> int:
        """checks whether latest guess is correct or max guesses is reached

        Returns:
            int: one of three class constant int values: LOSE_STATUS, WIN_STATUS, or IN_PROGRESS_STATUS
        """

        if self.check_solution():
            return self.Status.WIN
        elif len(self.guesses) == self.MAX_GUESSES:
            return self.Status.LOSE

        return self.Status.IN_PROGRESS
