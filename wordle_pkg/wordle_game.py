from . import console_ui
from . import word_bank


class WordleGame:
    """represents the game as a whole. contains methods to draw the board, validate guesses, 
    and check for victory condition
    """

    def __init__(self):
        self.is_active = True
        self.guesses = []
        self.solution = word_bank.generate_word()  # self.generate_word()
        self.latest_guess_letters = []  # list of WordleLetters
        self.latest_guess_string = ""

    def add_guess(self, validated_guess: str) -> None:
        """append guess to guesses list"""
        self.guesses.append(validated_guess)

    def draw_board(self) -> None:
        """use console_ui to print board"""
        console_ui.print_console_board(self.guesses)

    def validate_guess(self, user_guess: str) -> bool:
        """checks that a guess is a 5 letter alpha str

        Args:
            previous_guesses (list): words already present on the board
            cur_guess (str): word to be validated

        Returns:
            bool: True if valid, otherwise False
        """

        if len(user_guess) == 5 and user_guess.isalpha():
            # check whether already guessed
            if user_guess not in self.guesses:
                self.latest_guess_string = user_guess
                return True
            print("You already guessed that!")
        print("5 letter words ONLY!")

        return False

    def process_valid_guess(self, user_guess) -> None:
        """compares a given guess and solution to generate a list of WordleLetter instances
        which have appropriate correctness values

        Args:
            user_guess (str): valid word guessed by user
            solution_word (str): correct word

        """

        # clear latest_guess and update list of guessed words
        self.latest_guess_letters.clear()
        self.add_guess(user_guess)

        for idx, letter in enumerate(user_guess):
            # check for perfect match
            if letter == self.solution[idx]:
                # add WL object with CORRECT value to list
                self.latest_guess_letters.append(
                    WordleLetter(letter, WordleLetter.CORRECT))
            elif letter in self.solution:
                self.latest_guess_letters.append(
                    WordleLetter(letter, WordleLetter.PARTIAL))
            else:
                self.latest_guess_letters.append(
                    WordleLetter(letter, WordleLetter.WRONG))

    def check_solution(self) -> bool:
        """checks whether the latest guess is totally correct

        Returns:
            _type_: _description_
        """

        # if any letter isn't correct, return false
        for letter in self.latest_guess_letters:
            if letter.correctness != WordleLetter.CORRECT:
                return False
        return True


class WordleLetter:
    """represents a letter tile. class defines valid letters, correctness values, and comparison between instances
    """
    CORRECT = 1
    WRONG = 0
    PARTIAL = -1
    CORRECTNESS_VALUES = [CORRECT, WRONG, PARTIAL, None]
    ACCEPTED_LETTERS = "abcdefhijklmnopqrstuvwxyz"

    def __init__(self, letter: str, correctness=None):
        """constructor"""
        self._letter = self.letter_setter(letter)
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
        print('letter getter called')
        return self._letter

    def letter_setter(self, letter):
        """weird custom setter since constructor doesn't call actual property setters"""
        print('letter setter called')
        lower_letter = letter.lower()
        if lower_letter not in self.ACCEPTED_LETTERS:
            raise ValueError
        return lower_letter
