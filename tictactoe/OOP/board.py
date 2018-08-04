import copy

WINNING_POSITIONS = [(0, 4, 8), (2, 4, 6), # diagonal
                     (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
                     (0, 3, 6), (1, 4, 7), (2, 5, 8)] # columns

class Board(object):
    def __init__(self):
        self.board = [""] * 9


    def render_board():
        print "\n+--+--+--+\n".join([
               " {} | {} | {} ".format(self.board[0], self.board[1], self.board[2]),
               " {} | {} | {} ".format(self.board[3], self.board[4], self.board[5]),
               " {} | {} | {} ".format(self.board[6], self.board[7], self.board[8])]) + "\n"


    def copy_board():
        return copy.deepcopy(self.board)
