"""
[Module] Tic-tac-toe bot utilities.
"""
from random import randint
import requests


API_URL = "http://127.0.0.1:8000"


def is_registry_open() -> bool:
    """
    Checks if registry is available via API.
    """
    res = requests.get("{}/registry".format(API_URL))

    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def register_user(name: str) -> str:
    """
    Registers user in API game.
    """
    res = requests.post("{}/register_player/{}".format(API_URL, name))
    player_id = res.text
    return player_id


def is_my_turn(player_id: str) -> bool: 
    """
    Checks if it is our turn via API.
    """
    res = requests.get("{}/turn/{}".format(API_URL, player_id))
    
    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def read_board() -> list:
    """
    Gets game board via API.
    """
    res = requests.get("{}/board".format(API_URL))
    board = list(res.text)
    return board


def decide_move(board: list, player: str) -> [int, int]:
    """
    Decides next move to make.
    """
    row = randint(0, 2)
    column = randint(0, 2)
    return [row, column]


def validate_move(board: list, move: list) -> bool:
    """
    Checks if the move made is valid.
    """
    row, col = move[0], move[1]

    if board[row][col] is None:
        return True

    return False


def send_move(player_id: str, move: list) -> None:
    """
    Sends move to API.
    """
    row, col = move[0], move[1]
    res = requests.post("{}/move/{}/{}/{}".format(API_URL, player_id, row, column))
    return None


def does_game_continue() -> bool:
    """
    Checks if the current match continues via API.
    """
    res = requests.get("{}/continue".format(API_URL))

    if res.text == "true":
        return True
    elif res.text == "false":
        return False
