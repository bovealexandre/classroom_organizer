from random import shuffle

from colorama import Fore, Style


class Symbol:
    def __init__(self, color: str, icon: str) -> None:
        """Initialize a Symbol object.

        Args:
            color (str): The color of the symbol.
            icon (str): The icon associated with the symbol.
        """
        self.color: str = color
        self.icon: str = icon


class Card(Symbol):
    def __init__(self, color: str, icon: str, value: str) -> None:
        """Initialize a Card object.

        Args:
            color (str): The color of the card.
            icon (str): The icon associated with the card.
            value (str): The value of the card.
        """
        super().__init__(color, icon)
        self.value: str = value

    def __str__(self) -> str:
        """Return a string representation of the card with color formatting."""
        return f"{Fore.RED if self.color == 'red' else Fore.BLACK} {self.value} {self.icon} {Style.RESET_ALL}"

    def __repr__(self) -> str:
        """Return a string representation of the card with color formatting."""
        return f"{Fore.RED if self.color == 'red' else Fore.BLACK} {self.value} {self.icon} {Style.RESET_ALL}"

    def __lt__(self, other) -> bool:
        values: list[str] = [
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
        ]

        return values.index(self.value) < values.index(other.value)


class Deck:
    def __init__(self) -> None:
        """Initialize a Deck object with an empty list of cards."""
        self.cards: list[Card] = []

    def __str__(self):
        """Return a string representation of the deck."""
        return self.cards[::]

    def fill_deck(self) -> None:
        """Fill the deck with a standard set of playing cards."""
        color: list[str] = ["red", "black"]
        icon: list[str] = ["♥", "♦", "♣", "♠"]
        values: list[str] = [
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
        ]

        for card in values:
            for symbol in icon:
                self.cards.append(
                    Card(
                        color[0] if symbol == "♥" or symbol == "♦" else color[1],
                        symbol,
                        card,
                    )
                )

    def shuffle(self) -> None:
        """Shuffle the deck of cards."""
        shuffle(self.cards)

    def distribute(self, players) -> None:
        """Distribute cards from the deck to a list of players.

        Args:
            players (list): A list of player objects.
        """
        num_players: int = len(players)
        cards_per_player: int = len(self.cards) // num_players

        for player in players:
            player.cards = self.cards[:cards_per_player]
            player.number_of_cards = cards_per_player
            del self.cards[:cards_per_player]
