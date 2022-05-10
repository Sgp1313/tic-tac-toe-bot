'''
Main script.
'''

from time import sleep 
import requests
import utils


def main():

    name = 'Angel'
    print('------- Starting tic-tac-toe bot -------')
    sleep(1)

    # Register-phase begins
    registry_available = utils.is_registry_available()

    while not registry_available:
        sleep(5)

    player_id = utils.register_user(name)
    print("Player ID:", player_id)
    # Register-phase ends, game-phase begins
    game_continues = True

    while game_continues:

        my_turn = utils.is_my_turn(player_id)
        
        while not my_turn:
            print("My turn:", my_turn)
            sleep(5)
            my_turn = utils.is_my_turn(player_id)

        print("My turn:", my_turn)
        board = utils.read_board()
        print("Board:", board)
        is_move_valid = False

        while not is_move_valid:

            next_move = utils.decide_move(board, player_id)
            print("Move:", next_move)
            is_move_valid = utils.validate_move(board, next_move)

        utils.send_move(next_move)
        game_continues = utils.does_game_continue()
        sleep(5)


if __name__ == '__main__':
    main()
