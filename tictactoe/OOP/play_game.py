from board import Board
from players import Player
from game_engine import Engine

def main():
    human = Player()
    computer = Player("param")
    board = Board()
    game = Game(board, human, computer)
    game.play()
