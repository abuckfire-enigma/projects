import utilities
import logic

def get_human_move(board):
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
        if board[move - 1]:
            print "That square is taken... you need to choose an empty square: "
            continue
        else: break
    return move - 1


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


def game_over(board, computer):
    """
    Checks the board to see if the same is over and who won
    Args:
        board (list): the tic tac toe board
        computer (str): marker for the computer ('x' or 'o')
    Returns:
        bool: True if the game is over, False otherwise
    """
    if logic.is_win(board, computer):
        print "Victory for the machine!"
        return True
    if logic.is_win(board, utilities.get_opposite_marker(computer)):
        print "Nice work human. You won."
        return True
    if logic.is_board_full(board):
        print "Draw. We were equally matched."
        return True
    return False

def play_game():
    tic_tac_toe_enabled = True
    while tic_tac_toe_enabled:
        human = get_human_marker()
        computer = utilities.assign_marker_to_computer(human)
        is_human_turn = utilities.does_human_start_game(human)
        print "Let's begin.\nHere is the board: "
        board = utilities.create_board()
        utilities.pretty_print_board(board)

        in_game = True
        while in_game:
            if is_human_turn:
                board[get_human_move(board)] = human
            if not is_human_turn:
                print "Computer is moving..."
                board[logic.computer_move(board, computer)] = computer

            utilities.pretty_print_board(board)
            is_human_turn = not is_human_turn

            if game_over(board, computer):
                in_game = False
                tic_tac_toe_enabled = play_again()

if __name__ == "__main__":
    play_game()
