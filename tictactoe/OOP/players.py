class Player(object):
    def __init__(self, marker, is_human):
        self.marker = marker
        self.is_first = True if marker == "x" else False

    def get_marker(self):
        return self.marker

    def get_is_first(self):
        return self.is_first


class HumanPlayer(Player):
    @staticmethod
    def get_human_move(self):
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

class ComputerPlayer(Player):
    def get_computer_move(self):
        pass