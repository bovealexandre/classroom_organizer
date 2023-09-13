from utils.player import Player
from utils.card import Deck


class Board:
    def __init__(self, players: list[Player]) -> None:
        self.players: list[Player] = players
        self.turn_count: int = 0
        self.active_cards: list = [None] * len(players)
        self.history_cards: list = []

    def start_game(self) -> None:
        deck: Deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        deck.distribute(self.players)

        while True:
            self.turn_count += 1
            print(f"Turn {self.turn_count}")

            for i, player in enumerate(self.players):
                card = player.play()
                self.active_cards[i] = card

            self.history_cards.extend(self.active_cards)
            print(self.active_cards)
            self.active_cards = [None] * len(self.players)

            print(len(self.history_cards))

            if all(player.number_of_cards == 0 for player in self.players):
                print("Game Over!")
                break
