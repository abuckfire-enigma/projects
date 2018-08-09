from board import Board
from players import Player
from game import Game

def assign_markers():
    """
    Prompt human for decision to be 'x' or 'o' until it inputs 'x' or 'o'
    Returns:
        str: x or o
    """
    while True:
        marker = raw_input("You can play as 'x' or 'o'. 'x' always goes first. Which will you be? ") 
        if marker in ["x", "o"]:
            return marker, "x" if marker == "o" else "o"
        print "That is not a valid player type. Choose 'x' or 'o': "

def main():
    game = Game()
    human_marker, computer_marker = assign_markers()
    game.play(Board(),
              Player(human_marker, True),
              Player(computer_marker, False))

if __name__ == "__main__":
    main()
