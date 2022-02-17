from wordle_pkg import console_ui


def test_print_console_board_with_no_guesses():
    """_summary_ expect 5 blank rows to be printed
    """
    previous_guesses = []
    blanks = console_ui.print_console_board(previous_guesses=previous_guesses)
    assert blanks is 5


def test_print_console_board_with_no_param():
    """_summary_ expect 5 blank rows to be printed
    """
    blanks = console_ui.print_console_board()
    assert blanks is 5


def test_print_console_board_with_two_guesses():
    """_summary_ expect 3 blank rows to be printed
    """
    previous_guesses = ["wordle", "wordle"]
    blanks = console_ui.print_console_board(previous_guesses=previous_guesses)
    assert blanks is 3


def test_print_console_board_with_five_guesses():
    """_summary_ expect 0 blank rows to be printed
    """
    previous_guesses = ["wordle", "wordle", "wordle", "wordle", "wordle"]
    blanks = console_ui.print_console_board(previous_guesses=previous_guesses)
    assert blanks is 0
