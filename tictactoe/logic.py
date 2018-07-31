import random
import sys

import utilities


def is_win(board, marker):
    """
    Checks to see if a move is a winning move
    Args:
        board (list): the tic tac toe board
        marker (str): "x" or "o"
    Returns:
        bool: True if winning move, False otherwise
    """
    for (i, j, k) in utilities.WINNING_POSITIONS:
        if board[i] == marker and board[i] == board[j] == board[k]:
            return True
    return False


def is_board_full(board):
    """
    If the board is full, returns True, otherwise False
    """
    return "" not in board


def game_over(board, computer):
    """
    Checks the board to see if the same is over and who won
    Args:
        board (list): the tic tac toe board
        computer (str): marker for the computer ('x' or 'o')
    Returns:
        bool: True if the game is over, False otherwise
    """
    if is_win(board, computer):
        print "Victory for the machine!"
        return True
    if is_win(board, utilities.get_opposite_marker(computer)):
        print "Nice work human. You won."
        return True
    if is_board_full(board):
        print "Draw. We were equally matched."
        return True
    return False


def check_win_in_one(board, marker, square):
    """
    If a square is empty, checks to see if a move is a winning move
    Args:
        board (list): the tic tac toe board
        marker (str): "x" or "o"
        square (int): the square to try and move to
    Returns:
        bool: True if winning move, False otherwise        
    """
    temp_board = utilities.copy_board(board)
    temp_board[square] = marker
    return is_win(temp_board, marker) 


def is_fork(board, marker, square):
    """
    Checks if a move is a 'fork' move. A fork leads to an
    impossible to prevent win if not prevented.
    Args:
        board (list): the tic tac toe board
        marker (str): "x" or "o"
        square (int): the square to try and move to
    Returns:
        bool: True if fork occurs, False otherwise
    """
    temp_board = utilities.copy_board(board)
    temp_board[square] = marker
    return len(filter(lambda x: check_win_in_one(temp_board, marker, x), range(len(board)))) > 1


def computer_move(board, computer):
    """
    AI engine for the computer determining its next move.
    Args:
        board (list): the tic tac toe board
        marker (str): "x" or "o"
    Returns:
        int: the square the computer will move to        
    """
    board_squares = utilities.empty_squares(board)
    human_marker = utilities.get_opposite_marker(computer)

    # Offensive: can computer win in one
    for square in board_squares:
        if check_win_in_one(board, computer, square):
            return square

    # Defensive: can human win in one
    for square in board_squares:
        if check_win_in_one(board, human_marker, square):
            return square

    # Offensive: Can computer set up a fork
    for square in board_squares:
        if is_fork(board, computer, square):
            return square

    # Defensive: Can human set up a fork
    num_forks = 0
    t_move = -1
    for square in board_squares:
        if is_fork(board, human_marker, square):
            num_forks += 1
            t_move = square

    if num_forks == 1 or board[4] == human_marker:
        return t_move
    elif num_forks > 1:
        return random.choice(utilities.empty_side(board))

    # No offense/defense: try to center
    if not board[4]:
        return 4

    # otherwise, pick random spot
    return random.choice(utilities.empty_squares(board))
