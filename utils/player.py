from random import choice
from colorama import Fore, Style

from utils.card import Card


class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.cards: list[Card] = []
        self.turn_count: int = 0
        self.number_of_cards: int = 0
        self.history: list[Card] = []

    def play(self) -> Card:
        played_card: Card = choice(self.cards)
        print(
            f"{self.name} {self.turn_count} played: {Fore.RED if played_card.color == 'red' else Fore.BLACK} {played_card.value} {played_card.icon} {Style.RESET_ALL}"
        )
        self.cards.remove(played_card)
        self.turn_count += 1
        self.number_of_cards -= 1
        return played_card
