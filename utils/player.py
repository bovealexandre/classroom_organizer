from random import choice

from utils.card import Card


class Player:
    def __init__(self, name: str) -> None:
        """Initialize a Player object.

        Args:
            name (str): The name of the player.
        """
        self.name: str = name
        self.cards: list[Card] = []
        self.turn_count: int = 0
        self.number_of_cards: int = 0
        self.history: list[Card] = []
        self.points: int = 0

    def __str__(self) -> str:
        """Return a string representation of the player's state."""
        return """The player name is {self.name}
his cards are : {self.cards}
he is on turn : {self.turn_count}
he has {self.number_of_cards} cards
here is his history {self.history}""".format(
            self=self
        )

    def play(self) -> Card:
        """Simulate a player's turn, playing a random card from their hand.

        Returns:
            Card: The card played by the player.
        """
        print(f"{self.name}, here are your cards : {self.cards}")
        play_input: int = int(
            input(
                f"{self.name}, It's your turn ! What card do you want to play? (this takes an Int) : "
            )
        )
        played_card: Card = self.cards[play_input]
        # played_card: Card = choice(self.cards)
        print(f"{self.name} {self.turn_count} played: {played_card}")
        self.cards.remove(played_card)
        self.turn_count += 1
        self.number_of_cards -= 1
        return played_card

    def add_point(self) -> None:
        self.points += 1
