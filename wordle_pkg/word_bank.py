import random
# from wordle_game import WordleGame, WordleLetter


def generate_word():
    """return a random word from the defined list of 10
    Eventually should refactor to use some kind of Dictionary.com API

    Returns:
        str: 5 letter word from internal list
    """
    valid_words = ["crane", "power", 'slice', 'flier', 'eerie',
                   "drape", "slime", "brain", "plead", "gnarl"]

    return random.choice(valid_words)


# def validate_guess(previous_guesses, cur_guess):
#     """checks that a guess is a 5 letter alpha str

#     Args:
#         previous_guesses (list): words already present on the board
#         cur_guess (str): word to be validated

#     Returns:
#         bool: True if valid, otherwise False
#     """
#     if len(cur_guess) == 5 and cur_guess.isalpha():
#         # check whether already guessed
#         if cur_guess not in previous_guesses:
#             return True
#         else:
#             print("You already guessed that!")
#     else:
#         print("5 letter words ONLY!")

#     return False


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
