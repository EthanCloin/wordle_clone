import sys
from wordle_pkg.wordle_game import WordleGame


if __name__ == '__main__':
    # instantiate game object
    game = WordleGame()
    game.is_active = True

    # main game loop
    while game.is_active:
        # draw board
        game.draw_board()

        # loop until a valid word is guessed
        VALID_GUESS = False
        while not VALID_GUESS:
            VALID_GUESS = game.validate_guess(input(">> "))

        # update game obj with validated guess
        game.process_valid_guess(game.latest_guess_string)
        DID_WIN = game.check_solution()

        if DID_WIN:
            print("ayo")
            game.is_active = False
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
