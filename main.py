from random import choice
from utils.game import Board
from utils.player import Player


def choice_ai() -> bool:
    """
    Prompt the user to choose if a player will be controlled by AI or not and return a boolean value.

    Returns:
        bool: True if the user chooses 'Y' (yes) for AI, False if 'N' (no) is chosen.
    """
    while True:
        ai: str = input("Will it be an AI? (Y/N)").strip().upper()

        if ai == "Y":
            return True
        elif ai == "N":
            return False
        else:
            print("Please just write Y or N")


def choice_name(isAI: bool) -> str:
    """
    Generate a player's pseudonym based on whether the player is controlled by AI or not.

    Args:
        isAI (bool): True if the player is controlled by AI, False for human players.

    Returns:
        str: The generated pseudonym for the player.
    """
    pseudo: list[str] = [
        "Ace of Spades",
        "King of Hearts",
        "Queen of Diamonds",
        "Jack of Clubs",
        "Lucky Joker",
        "Card Shark",
        "Royal Flush",
        "Blackjack Pro",
        "Poker Face",
        "Diamond Dealer",
        "Hearts Master",
        "Spades Kingpin",
        "Club Captain",
        "Bridge Wizard",
        "Card Countess",
        "Deuce Duchess",
        "High Roller",
        "Wild Card",
        "Rummy Ace",
        "Solitaire Queen",
    ]
    if isAI:
        return choice(pseudo)
    else:
        return input("What pseudo would you like?")


if __name__ == "__main__":
    """
    Main block to start a card game with user-defined players.
    """
    while True:
        num_players: str = input("How many player do you want?")

        players: list[Player] = []

        if not num_players.isdigit():
            print("Please put a number!")
            continue
        if not (2 <= int(num_players) <= 52):
            print("Please put a number between 2 and 52")
            continue

        for player in range(0, int(num_players)):
            isAI: bool = choice_ai()
            player_name: str = choice_name(isAI)
            players.append(Player(player_name, isAI))

        board: Board = Board(players)

        board.start_game()
        break
