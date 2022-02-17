from wordle_pkg import word_bank, console_ui

if __name__ == '__main__':
    game_active = True
    words_guessed = []

    while game_active:
        console_ui.print_header()
        console_ui.print_console_board(words_guessed)

        current_guess = input()
