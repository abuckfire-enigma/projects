from board import Board
from players import Player
from game import Game

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

def main():
    human = Player(get_human_marker(), True)
    computer = Player(human.get_opponent, False)
    board = Board()
    board.render_board()
    game = Game()
    game.play(board, human, computer)

if __name__ == "__main__":
    main()
