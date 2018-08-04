class Game(object):
    def __init__(self, board):
        self.board = board
        self.human = assign_human_marker()
        self.computer = "o" if self.human == "x" else "x"

    @staticmethod
    def assign_human_marker():
        while True:
            marker = raw_input("You can play as 'x' or 'o'. 'x' always goes first. Which will you be? ") 
            if marker in ["x", "o"]:
                return marker
            print "That is not a valid player type. Choose 'x' or 'o': "


    def play_game():
        pass

