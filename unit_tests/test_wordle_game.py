from wordle_pkg.wordle_game import WordleGame, WordleLetter

TEST_GAME = WordleGame()
X_TEST_LETTER = WordleLetter('X')
Y_TEST_LETTER = WordleLetter('Y')


def test_adding_one_guess():
    """adds a word to guesses list
    """
    TEST_GAME.add_guess("testy")
    assert TEST_GAME.guesses[0] is "testy"


def test_validate_guess_five_letter_word():
    """checks that 5 letter word is accepted"""
    cur_guess = "doggo"
    assert TEST_GAME.validate_guess(cur_guess) is True


def test_validate_guess_three_letter_word():
    """checks that <5 letter words are rejected"""
    cur_guess = "dog"
    assert TEST_GAME.validate_guess(cur_guess) is False


def test_validate_guess_six_letter_word():
    """checks that >5 letter words are rejected"""
    cur_guess = "boring"
    assert TEST_GAME.validate_guess(cur_guess) is False


def test_validate_guess_number():
    """checks that non-alpha str are rejected"""
    cur_guess = "12345"
    assert TEST_GAME.validate_guess(cur_guess) is False


def test_find_one_matching_letter_in_wrong_location():
    """checks that the scoring function correctly identifies a letter that is cor"""
    TEST_GAME.solution = "words"
    cur_guess = "xwxxx"
    TEST_GAME.process_valid_guess(cur_guess)

    assert TEST_GAME.latest_guess_letters[0].correctness is WordleLetter.WRONG
    assert TEST_GAME.latest_guess_letters[1].correctness is WordleLetter.PARTIAL
    assert TEST_GAME.latest_guess_letters[2].correctness is WordleLetter.WRONG
    assert TEST_GAME.latest_guess_letters[3].correctness is WordleLetter.WRONG
    assert TEST_GAME.latest_guess_letters[4].correctness is WordleLetter.WRONG


def test_find_one_matching_letter_in_right_location():
    """checks that the scoring function correctly identifies a letter that is cor"""
    TEST_GAME.solution = "words"
    cur_guess = "wxxxx"
    TEST_GAME.process_valid_guess(cur_guess)

    assert TEST_GAME.latest_guess_letters[0].correctness is WordleLetter.CORRECT
    assert TEST_GAME.latest_guess_letters[1].correctness is WordleLetter.WRONG
    assert TEST_GAME.latest_guess_letters[2].correctness is WordleLetter.WRONG
    assert TEST_GAME.latest_guess_letters[3].correctness is WordleLetter.WRONG
    assert TEST_GAME.latest_guess_letters[4].correctness is WordleLetter.WRONG


def test_find_two_matching_letters_in_right_location():
    """checks that the scoring function correctly identifies two correct letters"""
    TEST_GAME.solution = "words"
    cur_guess = "wxxdx"
    TEST_GAME.process_valid_guess(cur_guess)

    assert TEST_GAME.latest_guess_letters[0].correctness is WordleLetter.CORRECT
    assert TEST_GAME.latest_guess_letters[1].correctness is WordleLetter.WRONG
    assert TEST_GAME.latest_guess_letters[2].correctness is WordleLetter.WRONG
    assert TEST_GAME.latest_guess_letters[3].correctness is WordleLetter.CORRECT
    assert TEST_GAME.latest_guess_letters[4].correctness is WordleLetter.WRONG


def test_detect_correct_word():
    """checks that guessing the solution results in True"""
    TEST_GAME.solution = "words"
    TEST_GAME.process_valid_guess("words")

    assert TEST_GAME.check_solution() is True


def test_detect_incorrect_word():
    """checks that guessing the wrong solution results in False"""
    TEST_GAME.solution = "xxxxx"
    TEST_GAME.process_valid_guess("words")

    assert TEST_GAME.check_solution() is False


def test_x_equal_to_x():
    """checks that WordleLetter instances with same value and different case are equal"""
    another_x_letter = WordleLetter('x')
    print(another_x_letter.letter, X_TEST_LETTER.letter)

    assert X_TEST_LETTER == another_x_letter


def test_x_unequal_to_y():
    """checks that WordleLetter instances with different values are uneqal"""
    assert X_TEST_LETTER != Y_TEST_LETTER
