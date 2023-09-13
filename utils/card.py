from random import shuffle


class Symbol:
    def __init__(self, color: str, icon: str) -> None:
        self.color: str = color
        self.icon: str = icon


class Card(Symbol):
    def __init__(self, color: str, icon: str, value: str) -> None:
        super().__init__(color, icon)
        self.value: str = value


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def fill_deck(self) -> None:
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
        shuffle(self.cards)

    def distribute(self, players) -> None:
        num_players: int = len(players)
        cards_per_player: int = len(self.cards) // num_players

        for player in players:
            player.cards = self.cards[:cards_per_player]
            player.number_of_cards = cards_per_player
            del self.cards[:cards_per_player]
