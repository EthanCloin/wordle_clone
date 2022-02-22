from wordle_pkg import word_bank
from wordle_pkg.wordle_game import WordleLetter, WordleGame


WORD_BANK = ["crane", "power", 'slice', 'flier', 'eerie',
             "drape", "slime", "brain", "plead", "gnarl"]


def test_generate_word():
    """verify that the generated word is present in the list of valid words"""
    word = word_bank.generate_word()
    assert word in WORD_BANK


# TODO: refactor this to go in a test_wordle_game.py file
def test_validate_guess_five_letter_word():
    """checks that 5 letter word is accepted"""
    previous_guesses = ["words"]
    cur_guess = "doggo"
    assert WordleGame.validate_guess(
        previous_guesses=previous_guesses, cur_guess=cur_guess) is True


def test_validate_guess_three_letter_word():
    """checks that <5 letter words are rejected"""
    previous_guesses = ["words"]
    cur_guess = "dog"
    assert WordleGame.validate_guess(
        previous_guesses=previous_guesses, cur_guess=cur_guess) is False


def test_validate_guess_six_letter_word():
    """checks that >5 letter words are rejected"""
    previous_guesses = ["words"]
    cur_guess = "boring"
    assert WordleGame.validate_guess(
        previous_guesses=previous_guesses, cur_guess=cur_guess) is False


def test_validate_guess_number():
    """checks that non-alpha str are rejected"""
    previous_guesses = ["wordle"]
    cur_guess = "12345"
    assert WordleGame.validate_guess(
        previous_guesses=previous_guesses, cur_guess=cur_guess) is False


def test_find_one_matching_letter_in_wrong_location():
    """checks that the scoring function correctly identifies a letter that is cor"""
    solution = "words"
    cur_guess = "xwxxx"
    returned_list = WordleGame.score_word(cur_guess, solution)

    assert returned_list[0].get_correctness() is WordleLetter.WRONG
    assert returned_list[1].get_correctness() is WordleLetter.PARTIAL
    assert returned_list[2].get_correctness() is WordleLetter.WRONG
    assert returned_list[3].get_correctness() is WordleLetter.WRONG
    assert returned_list[4].get_correctness() is WordleLetter.WRONG


def test_find_one_matching_letter_in_right_location():
    """checks that the scoring function correctly identifies a letter that is cor"""
    solution = "words"
    cur_guess = "wxxxx"
    returned_list = WordleGame.score_word(cur_guess, solution)

    assert returned_list[0].get_correctness() is WordleLetter.CORRECT
    assert returned_list[1].get_correctness() is WordleLetter.WRONG
    assert returned_list[2].get_correctness() is WordleLetter.WRONG
    assert returned_list[3].get_correctness() is WordleLetter.WRONG
    assert returned_list[4].get_correctness() is WordleLetter.WRONG


def test_find_two_matching_letters_in_right_location():
    """checks that the scoring function correctly identifies two correct letters"""
    solution = "words"
    cur_guess = "wxxdx"
    returned_list = WordleGame.score_word(cur_guess, solution)

    assert returned_list[0].get_correctness() is WordleLetter.CORRECT
    assert returned_list[1].get_correctness() is WordleLetter.WRONG
    assert returned_list[2].get_correctness() is WordleLetter.WRONG
    assert returned_list[3].get_correctness() is WordleLetter.CORRECT
    assert returned_list[4].get_correctness() is WordleLetter.WRONG


def test_detect_correct_word():
    solution = "words"
    cur_guess = "words"

    assert WordleGame.decide_outcome(cur_guess, solution) is True


def test_detect_incorrect_word():
    solution = "xxxxx"
    cur_guess = "words"

    assert WordleGame.check_solution(cur_guess) is False
