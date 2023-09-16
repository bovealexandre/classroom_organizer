from utils.card import Card, Deck
from utils.player import Player


class Board:
    def __init__(self, players: list[Player]) -> None:
        """Initialize a Board object.

        Args:
            players (list): A list of Player objects representing the players in the game.
        """
        self.players: list[Player] = players
        self.turn_count: int = 0
        self.active_cards: list[Card] = [] * len(players)
        self.history_cards: list[Card] = []

    def start_game(self) -> None:
        """Start and manage the game loop.

        This method initializes the deck, shuffles and distributes cards to players, and
        manages the turns until the game is over.
        """
        deck: Deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        deck.distribute(self.players)

        while True:
            self.turn_count += 1
            print(f"Turn {self.turn_count}")
            winning_player: int = 0

            for i, player in enumerate(self.players):
                card: Card = player.play()
                self.active_cards.append(card)
                if card > self.active_cards[winning_player]:
                    winning_player = i

            print(f"{self.players[winning_player].name} won the round")
            self.players[winning_player].add_point()
            self.history_cards.extend(self.active_cards)
            print(self.active_cards)
            self.active_cards = [] * len(self.players)

            print(len(self.history_cards))

            if all(player.number_of_cards == 0 for player in self.players):
                winner: Player = self.players[0]
                for p in self.players:
                    if p.points > winner.points:
                        winner = p
                print(f"The winner is {winner.name}")
                break
