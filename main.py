from utils.player import Player
from utils.game import Board

if __name__ == "__main__":
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    player3 = Player("Player 3")

    board: Board = Board([player1, player2, player3])

    board.start_game()
