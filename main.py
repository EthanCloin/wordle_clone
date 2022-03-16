import sys
from wordle_pkg.wordle_game import WordleGame, WordleWord, WordleLetter


if __name__ == '__main__':
    # instantiate game object
    game = WordleGame("right")

    # main game loop
    while game.is_active:
        # draw board
        game.draw_board()
        game.accept_input()

        # update game obj with validated guess
        game_status = game.check_game_over()

        if game_status is WordleGame.Status.IN_PROGRESS:
            continue
        elif game_status is WordleGame.Status.LOSE:
            game.draw_board()
            print("Loser")
            break
        elif game_status is WordleGame.Status.WIN:
            game.draw_board()
            print("Winner")
            break
