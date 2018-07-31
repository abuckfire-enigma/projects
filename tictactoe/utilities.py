import copy
import random

WINNING_POSITIONS = [(0, 4, 8), (2, 4, 6), # diagonal
                     (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
                     (0, 3, 6), (1, 4, 7), (2, 5, 8)] # columns


def create_board():
    """
    Create a tic tac toe board as a list with 9 empty string values
    Returns: list
    """
    return [""] * 9


def pretty_print_board(board):
    """
    print the tic tac toe board in a human-friendly format
    Args:
        board (list): the tic tac toe board
    """
    print "\n+--+--+--+\n".join([
           " {} | {} | {} ".format(board[0], board[1], board[2]),
           " {} | {} | {} ".format(board[3], board[4], board[5]),
           " {} | {} | {} ".format(board[6], board[7], board[8])]) + "\n"

def copy_board(board):
    """
    Copies the current tic tac toe board
    Args:
        board (list): the tic tac toe board
    list: copy of the tic tac toe board
    """
    return copy.deepcopy(board)

def assign_marker_to_computer(human_marker):
    """
    Based on human input, get the computer marker
    Args:
        human_marker (str): x or o
    Returns:
        str: x or o
    """
    return "o" if human_marker == "x" else "x"

def does_human_start_game(human_marker):
    """
    If the human chose to be player x, it goes first
    Args:
        human_marker (str): x or o
    Returns:
        bool: True if x, else False
    """
    return True if human_marker == "x" else False

def empty_squares(board):
    """
    Gets list of empty squares in the board
    Args:
        board (list): the tic tac toe board
    """
    return empty_corner(board) + empty_side(board)


def empty_side(board):
    """
    Gets list of empty squares in the board
    Args:
        board (list): the tic tac toe board
    """
    return [square for square in range(1, len(board), 2) if not board[square]]

def empty_corner(board):
    """
    Gets list of empty squares in the board
    Args:
        board (list): the tic tac toe board
    """
    return [square for square in range(0, len(board), 2) if not board[square]]

def get_opposite_marker(player):
    """
    Get the marker for the opposite player
    Args:
        player (str): x or o
    Return:
        str: x or o
    """
    return "x" if player == "o" else "o"

def get_human_move(board):
    """
    Prompt human for next move until the move is
        - in the correct format
        - for a position that is not taken
    Args:
        board (list): the tic tac toe board
        marker (str): "x" or "o"
    Return:
        int: Square the human wants to move to        
    """
    while True:
        try:
            move = int(raw_input("Choose a square 1-9: "))
        except ValueError:
            print "That was not a number 1 to 9! Try again: "
            continue
        if board[move - 1]:
            print "That square is taken... you need to choose an empty square: "
            continue
        else: break
    return move - 1


def get_human_marker():
    """
    Prompt human for decision to be 'x' or 'o' until it inputs 'x' or 'o'
    Returns:
        str: x or o
    """
    while True:
        marker = raw_input("You can play as 'x' or 'o'. 'x' always goes first. Which will you be? ") 
        if marker in ["x", "o"]:
            return marker
        print "That is not a valid player type. Choose 'x' or 'o': "


def play_again():
    """
    Prompt human for decision to play again or not until it inputs 'yes' or 'no'
    Returns:
        bool: True if play again ('yes'), False otherwise ('no')
    """
    while True:
        again = raw_input("Care to play again (yes/no)? ")
        if again in ["yes", "no"]:
            return False if again == "no" else True
        print "Not a valid response. Type 'yes' or 'no': "
