import copy

WINNING_POSITIONS = [(0, 4, 8), (2, 4, 6), # diagonal
                     (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
                     (0, 3, 6), (1, 4, 7), (2, 5, 8)] # columns

class Board(object):
    def __init__(self):
        self.board = [""] * 9


    def render_board(self):
        print "\n+--+--+--+\n".join([
               " {} | {} | {} ".format(self.board[0], self.board[1], self.board[2]),
               " {} | {} | {} ".format(self.board[3], self.board[4], self.board[5]),
               " {} | {} | {} ".format(self.board[6], self.board[7], self.board[8])]) + "\n"

    def get_board(self):
        return self.board

    def copy_board(self):
        return copy.deepcopy(self.board)

    def is_empty(self, square):
        return True if self.board[square] else False

    def board_full(self):
        """
        If the board is full, returns True, otherwise False
        """
        return "" not in self.board

    def marker_at_square(self, square):
        return self.board[square]

    def center_empty(self):
        return "" in self.board[4]

    def empty_squares(self):
        """
        Gets list of empty squares in the board
        """
        return self.empty_corner() + self.empty_side()

    def empty_side(self):
        """
        Gets list of empty squares in the board
        """
        return [square for square in range(1, len(self.board), 2) if not self.board[square]]

    def empty_corner(self):
        """
        Gets list of empty squares in the board
        """
        return [square for square in range(0, len(self.board), 2) if not self.board[square]]


    def update_board(self, move, marker):
        self.board[move] = marker

    def is_win(self):
        """
        Checks to see if a move is a winning move
        Args:
            board (list): the tic tac toe board
            marker (str): "x" or "o"
        Returns:
            bool: True if winning move, False otherwise
        """
        for (i, j, k) in WINNING_POSITIONS:
            if self.board[i] != "" and self.board[i] == self.board[j] == self.board[k]:
                return self.board[i]
