import random


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
