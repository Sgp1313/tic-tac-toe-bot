'''
Utils module.
'''
from random import randint

def is_registry_available() -> bool:
    '''
    Returns: True | False
    '''

    is_available = True
    return is_available


def register_user(name: str) -> int:
    '''
    Returns: str [player ID]
    '''

    player = "X"
    return player


def is_my_turn(player: str) -> bool: 
    '''
    Returns: True | False
    '''
    my_turn = True
    pass my_turn


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
    x = randint(0, 3)
    y = randint(0, 3)

    return [x, y]


def validate_move(board: list, move: list) -> bool:
    '''
    Returns: True | False
    '''
    x, y = board[move[0]], board[move[1]]

    if board[x][y] is None:
        return True

    return False


def send_move():
    
    # Sending move
    return True


def does_game_continue() -> bool:
    '''
    Returns: True | False
    '''
    game_continues = True
    return game_continues
