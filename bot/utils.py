'''
[Module] Tic-tac-toe bot utilities.
'''

from random import randint
import requests


def is_registry_open() -> bool:
    '''
    Checks if registry is available via API.
    '''
    res = requests.get('http://127.0.0.1:8000/registry')

    if res.text == 'true':
        is_open = True
    elif res.text == 'false':
        is_open = False

    return is_open


def register_user(name: str) -> str:
    '''
    Registers user in API game.
    '''
    res = requests.post('http://127.0.0.1:8000/register_player/{}'.format(name))
    player_id = res.text

    return player_id


def is_my_turn(player_id: str) -> bool: 
    '''
    Checks player's turn via API.
    '''
    res = requests.get('http://127.0.0.1:8000/turn/{}'.format(player_id))
    
    if res.text == 'true':
        my_turn = True
    elif res.text == 'false':
        my_turn = False

    return my_turn


def read_board() -> list:
    '''
    Returns: 3x3 matrix list
    '''
    board = [[None, None, None], [None, None, None], [None, None, None]]
    return board


def decide_move(board: list, player: str) -> [int, int]:
    '''
    Returns: a list of two ints
    '''
    x = randint(0, 2)
    y = randint(0, 2)

    return [x, y]


def validate_move(board: list, move: list) -> bool:
    '''
    Returns: True | False
    '''
    # x = fila, y = columna
    x, y = move[0], move[1]

    if board[x][y] is None:
        return True

    return False


def send_move(move: list) -> None:
    
    # Sending move
    return None


def does_game_continue() -> bool:
    '''
    Returns: True | False
    '''
    game_continues = True
    return game_continues


# print(is_registry_open(), type(is_registry_open()))
# print(register_user("Pedro"))
print(is_my_turn("O"))
