from . import console_ui
from . import word_bank
# import console_ui


class WordleGame:
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
            else:
                print("You already guessed that!")
        else:
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
            if letter.get_correctness() != WordleLetter.CORRECT:
                return False
        return True


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


# def score_word(user_guess, solution_word) -> list[WordleLetter]:
#     """compares a given guess and solution to generate a list of WordleLetter instances
#     which have appropriate correctness values

#     Args:
#         user_guess (str): valid word guessed by user
#         solution_word (str): correct word

#     Returns:
#         list[WordleLetter]: five WordleLetter objects with appropriate correctness values
#     """

#     wordle_letter_list = []
#     for idx, letter in enumerate(user_guess):
#         # check for perfect match
#         if letter == solution_word[idx]:
#             # add WL object with CORRECT value to list
#             wordle_letter_list.append(
#                 WordleLetter(letter, WordleLetter.CORRECT))
#         elif letter in solution_word:
#             wordle_letter_list.append(
#                 WordleLetter(letter, WordleLetter.PARTIAL))
#         else:
#             wordle_letter_list.append(WordleLetter(letter, WordleLetter.WRONG))

#     return wordle_letter_list


# def decide_outcome(user_guess, solution_word) -> bool:
#     """checks whether every letter matches the solution word

#     Args:
#         user_guess (_type_): valid word guessed by user
#         solution_word (_type_): correct word

#     Returns:
#         bool: _description_
#     """

#     # get list of WordleLetters
#     wordle_letter_list = score_word(user_guess, solution_word)

#     # if any letter isn't correct, return false
#     for letter in wordle_letter_list:
#         if letter.get_correctness() != WordleLetter.CORRECT:
#             return False
#     return True
