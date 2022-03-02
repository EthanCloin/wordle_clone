import sys
from wordle_pkg.wordle_game import WordleGame


if __name__ == '__main__':
    # instantiate game object
    game = WordleGame("right")
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
        game.process_valid_guess()
        game_status = game.check_game_over()

        if game_status is WordleGame.IN_PROGRESS_STATUS:
            continue
        elif game_status is WordleGame.LOSE_STATUS:
            game.draw_board()
            print("Loser")
            break
        elif game_status is WordleGame.WIN_STATUS:
            game.draw_board()
            print("Winner")
            break

        # if DID_WIN:
        #     print("ayo")
        #     game.is_active = False
        #     break
        # else:
        #     print("oof")
