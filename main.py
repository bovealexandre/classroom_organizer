from utils.game import Board
from utils.player import Player

if __name__ == "__main__":
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    player3 = Player("Player 3")
    player4 = Player("Player 4")
    player5 = Player("Player 5")

    board: Board = Board([player1, player2, player3, player4, player5])

    board.start_game()
