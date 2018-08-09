class Game(object):
    def __init__(self):
        pass

    def play_again(self):
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

    @staticmethod
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

    def cue_start_game(self, human, computer):
        print "Let's begin: Human is ", human.get_marker(), " and computer is ", computer.get_marker()

    def game_over(self, board):
        if board.is_win():
            print "We have a winner!: Player", board.is_win()
            return True
        if board.board_full():
            print "CATS game"
            return True
        return False

    def play(self, board, human, computer):
        is_human_turn = human.get_is_first()
        self.cue_start_game(human, computer)
        while not self.game_over(board):
            if is_human_turn:
                board.update_board(human.get_move(board), human.get_marker())
            if not is_human_turn:
                board.update_board(computer.get_move(board), computer.get_marker())
            board.render_board()
            is_human_turn = not is_human_turn
