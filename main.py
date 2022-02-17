from wordle_pkg import word_bank, console_ui

if __name__ == '__main__':
    game_active = True
    words_guessed = []

    while game_active:
        console_ui.print_header()
        console_ui.print_console_board(words_guessed)

        valid_guess = False
        cur_guess = ""
        while not valid_guess:
            cur_guess = input(">> ")
            valid_guess = word_bank.validate_guess(
                previous_guesses=words_guessed, cur_guess=cur_guess)

        words_guessed.append(cur_guess)
