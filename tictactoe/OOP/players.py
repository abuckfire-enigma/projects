import copy
import random
from board import WINNING_POSITIONS


class Player(object):
    def __init__(self, marker, is_human):
        self.marker = marker
        self.is_first = True if marker == "x" else False
        self.is_human = is_human
        self.opponent = "x" if self.marker == "o" else "o"

    def get_marker(self):
        return self.marker

    def get_is_first(self):
        return self.is_first

    def get_opponent(self):
        return self.opponent

    def get_move(self, board):
        if self.is_human:
            return self.ask_for_move(board)
        return self.computer_move(board)

    def ask_for_move(self, board):
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
            if board.is_empty(move - 1):
                print "That square is taken... you need to choose an empty square: "
                continue
            else: break
        return move - 1

    def computer_move(self, board):
        """
        AI engine for the computer determining its next move.
        Args:
            board (list): the tic tac toe board
            marker (str): "x" or "o"
        Returns:
            int: the square the computer will move to        
        """
        # Check if win in one
        for square in board.empty_squares():
            if self.check_win_in_one(board.get_board(), square):
                return square

        # Offensive: Can computer set up a fork
        for square in board.empty_squares():
            if self.is_fork(board.get_board(), self.marker, square):
                return square

        # Defensive: Can human set up a fork
        num_forks = 0
        t_move = -1
        for square in board.empty_squares():
            if self.is_fork(board.get_board(), self.opponent, square):
                num_forks += 1
                t_move = square

        if num_forks == 1 or board.marker_at_square(4) == self.opponent:
            return t_move
        elif num_forks > 1:
            return random.choice(board.empty_side())

        # No offense/defense: try to center
        if not board.center_empty():
            return 4

        # otherwise, pick random spot
        return random.choice(board.empty_squares())

    def is_win(self, board, marker):
        """
        Checks to see if a move is a winning move
        Args:
            board (list): the tic tac toe board
            marker (str): "x" or "o"
        Returns:
            bool: True if winning move, False otherwise
        """
        for (i, j, k) in WINNING_POSITIONS:
            if board[i] == marker and board[i] == board[j] == board[k]:
                return True
        return False

    def check_win_in_one(self, board, square):
        """
        If a square is empty, checks to see if a move is a winning move
        Args:
            board (list): the tic tac toe board
            marker (str): "x" or "o"
            square (int): the square to try and move to
        Returns:
            bool: True if winning move, False otherwise        
        """
        temp_board_1 = copy.deepcopy(board)
        temp_board_2 = copy.deepcopy(board)
        temp_board_1[square] = self.marker
        temp_board_2[square] = self.opponent
        return self.is_win(temp_board_1, self.marker) or self.is_win(temp_board_2, self.opponent)


    def is_fork(self, board, marker, square):
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
        temp_board = copy.deepcopy(board)
        temp_board[square] = marker
        return len(filter(lambda x: self.check_win_in_one(temp_board, x), range(len(temp_board)))) > 1
