from wordle_pkg import word_bank

WORD_BANK = ["crane", "power", 'slice', 'flier', 'eerie',
             "drape", "slime", "brain", "plead", "gnarl"]


def test_generate_word():
    """verify that the generated word is present in the list of valid words"""
    word = word_bank.generate_word()
    assert word in WORD_BANK


def test_validate_guess_five_letter_word():
    """checks that 5 letter word is accepted"""
    previous_guesses = ["wordle"]
    cur_guess = "doggo"
    assert word_bank.validate_guess(
        previous_guesses=previous_guesses, cur_guess=cur_guess) is True


def test_validate_guess_three_letter_word():
    """checks that <5 letter words are rejected"""
    previous_guesses = ["wordle"]
    cur_guess = "dog"
    assert word_bank.validate_guess(
        previous_guesses=previous_guesses, cur_guess=cur_guess) is False


def test_validate_guess_six_letter_word():
    """checks that >5 letter words are rejected"""
    previous_guesses = ["wordle"]
    cur_guess = "boring"
    assert word_bank.validate_guess(
        previous_guesses=previous_guesses, cur_guess=cur_guess) is False


def test_validate_guess_number():
    """checks that non-alpha str are rejected"""
    previous_guesses = ["wordle"]
    cur_guess = "12345"
    assert word_bank.validate_guess(
        previous_guesses=previous_guesses, cur_guess=cur_guess) is False
