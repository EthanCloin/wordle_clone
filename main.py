from wordle_pkg.wordle_game import WordleGame

if __name__ == '__main__':
    game = WordleGame()
    game.is_active = True
    # WordleGame().check_guess(guess='guess')
    while game.is_active:
        game.draw_board()

        valid_guess = False
        while not valid_guess:
            valid_guess = game.validate_guess(input(">> "))

        game.process_valid_guess(game.latest_guess_string)
        didWin = game.check_solution()
        if didWin:
            print("ayo")
            exit(0)
        else:
            print("oof")

    # words_guessed = []

    # while game_active:
    #     console_ui.print_header()
    #     console_ui.print_console_board(words_guessed)

    #     valid_guess = False
    #     while not valid_guess:
    #         cur_guess = input(">> ")
    #         valid_guess = word_bank.validate_guess(
    #             previous_guesses=words_guessed, cur_guess=cur_guess)

    #     words_guessed.append(cur_guess)
