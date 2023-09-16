from random import choice

from utils.card import Card


class Player:
    def __init__(self, name: str, isAI: bool) -> None:
        """Initialize a Player object.

        Args:
            name (str): The name of the player.
            isAI (bool): Boolean to check if the player is an AI.
        """
        self.name: str = name
        self.cards: list[Card] = []
        self.turn_count: int = 0
        self.number_of_cards: int = 0
        self.history: list[Card] = []
        self.points: int = 0
        self.isAI: bool = isAI

    def __str__(self) -> str:
        """Return a string representation of the player's state."""
        return """The player name is {self.name}
his cards are : {self.cards}
he is on turn : {self.turn_count}
he has {self.number_of_cards} cards
here is his history {self.history}""".format(
            self=self
        )

    def __lt__(self, other) -> bool:
        return self.points < other.points

    def play(self) -> Card:
        """Simulate a player's turn, playing a random card from their hand.

        Returns:
            Card: The card played by the player.
        """

        while True:
            played_card: Card
            if self.isAI:
                played_card = choice(self.cards)
            else:
                print(f"{self.name}, here are your cards : {self.cards}")
                play_input: str = input(
                    f"{self.name}, It's your turn ! What card do you want to play? (this takes an Int) : "
                )

                if not play_input.isdigit():
                    print("Please put a number!")
                    continue
                if 0 >= int(play_input) > len(self.cards):
                    print(
                        f"Please put a number between 0 and {str(len(self.cards)-1)}!"
                    )
                    continue

                played_card = self.cards[int(play_input)]

            print(f"{self.name} {self.turn_count} played: {played_card}")
            self.cards.remove(played_card)
            self.turn_count += 1
            self.number_of_cards -= 1
            return played_card

    def add_point(self) -> None:
        """Increment the player's points by 1."""
        self.points += 1
