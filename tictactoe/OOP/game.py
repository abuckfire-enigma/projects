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

    def prompt_player(self, player):
        print "It is your turn player ", player.get_marker()

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

    def cue_start_game(self, human, computer):
        print "Let's begin: Human is ", human.get_marker(), " and computer is ", computer.get_marker()

    def play(self, board, human, computer):
        tic_tac_toe_enabled = True
        while tic_tac_toe_enabled:
            is_human_turn = human.get_is_first()
            self.cue_start_game(human, computer)
            in_game = True
            while in_game:
                if is_human_turn:
                    self.prompt_player(human)
                    board.update_board(human.get_move(board), human.get_marker())

                if not is_human_turn:
                    print "Computer is moving..."
                    computer_move = computer.get_move(board)
                    board.update_board(computer.get_move(board), computer.get_marker())

                board.render_board()
                is_human_turn = not is_human_turn
                

                if board.is_board_full() or pla.game_over():
                    in_game = False
                    tic_tac_toe_enabled = play_again()
