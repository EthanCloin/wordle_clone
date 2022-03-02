def print_console_board(previous_guesses=[]):
    """_summary_ shows the board on console including any previous valid guesses

    Args:
        previous_guesses (list, optional): _description_. Defaults to [].

    Returns:
        int: the number of blank rows printed
    """

    # print previous guesses
    for word in previous_guesses:
        print(word)

    remaining_row_count = 6 - len(previous_guesses)
    for _ in range(0, remaining_row_count):
        for _ in range(0, 5):
            print('_', end=" ")
        print('\n')
    return remaining_row_count


def print_header():
    print("W O R D L E ")
    print('<>'*6)
    print()


def print_victory_message():
    print("CONGRATULATIONS, YOU GOT THE WORD!")


def print_defeat_message():
    print("Oh No...better luck next time!")
