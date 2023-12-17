from rich.console import Console
from rich.table import Table

console = Console()

VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
    'Spades': '♠️',
    'Clubs': '♣️',
    'Diamonds': '♦️',
    'Hearts': '♥️'
}


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return self.value + SUITS_UNI[self.suit]

    def __repr__(self):
        return str(self)

    def __eq__(self, other_card) -> bool:
        return self.suit == other_card.suit and self.value == other_card.value

    def __gt__(self, other_card) -> bool:
        if SUITS.index(self.suit) == SUITS.index(other_card.suit):
            return VALUES.index(self.value) > VALUES.index(other_card.value)

    def __lt__(self, other_card) -> bool:
        if SUITS.index(self.suit) == SUITS.index(other_card.suit):
            return VALUES.index(self.value) < VALUES.index(other_card.value)


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(value, suit))

    def __str__(self):
        return ' '.join(str(card.value) + SUITS_UNI[card.suit] for card in self.cards)

    def __repr__(self):
        return str(self)

    def show(self):
        print(f'deck[{len(self.cards)}]:', end=' ')
        print(*self.cards, sep=', ')

    def draw(self, x):
        x *= x > 0
        drawn_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return drawn_cards

    def shuffle(self):
        import random
        random.shuffle(self.cards)


def player_number(player):
    if player % 2 == 0:
        return 2
    return 1


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1_hand = self.deck.draw(10)
        self.player2_hand = self.deck.draw(10)
        self.table_cards = []

    def draw_to_ten(self, hand):
        while len(hand) < 10:
            card = self.deck.draw(1)[0]  # Берем первый (и единственный) элемент списка
            if card:
                hand.append(card)
            else:
                break  # Выход из цикла, если колода пуста

    def show_table(self):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Attack", style="dim", width=20)
        table.add_column("Game", justify="center", width=20)
        table.add_column("Defense", style="dim", width=20)

        for i in range(max(len(self.player1_hand), len(self.table_cards), len(self.player2_hand))):
            p1_card = f"{i + 1}. {str(self.player1_hand[i])}" if i < len(self.player1_hand) else ""
            table_card = f"{i + 1}. {str(self.table_cards[i])}" if i < len(self.table_cards) else ""
            p2_card = f"{i + 1}. {str(self.player2_hand[i])}" if i < len(self.player2_hand) else ""

            table.add_row(p1_card, table_card, p2_card)

        console.print(table)

    def play(self):
        player1_first_turn = True
        player1_turn = True
        # player1_hand = [...]
        # player2_hand = [...]
        player = 1
        while True:
            next_round = False
            while not next_round:
                if player1_turn:
                    if player1_first_turn:
                        player1_move = min(self.player1_hand)
                        print("Игрок атакует 1 картой ", player1_move)
                        self.player1_hand.remove(player1_move)
                        self.table_cards.append(player1_move)
                        self.show_table()
                        player1_first_turn = False
                        player1_turn = False
                        player2_turn = True
                        player += 1
                    else:  # не первый ход
                        self.show_table()
                        if (self.table_cards and
                            not any(card.value in [player_card.value for player_card in self.player1_hand] for card in self.table_cards)):
                            self.table_cards = []
                            next_round = True
                            player1_turn = True
                            player2_turn = False
                            console.print(f"Игроку {player_number(player)} нечего подкидывать")
                            player += 1
                        elif self.table_cards and any(card.value in [player_card.value for player_card in self.player1_hand] for card in self.table_cards):
                            player_input = int(input(f"Игрок {player_number(player)} атакует. Введи индекс карты в руке: "))
                            player1_move = self.player1_hand[player_input - 1]
                            if player1_move.value in [card.value for card in self.table_cards]:
                                console.print(f"Игрок {player_number(player)} выложил на стол карту: [bold]{player1_move}[/bold]")
                                self.player1_hand.remove(player1_move)
                                self.table_cards.append(player1_move)
                                self.show_table()
                                player1_turn = False
                                player2_turn = True
                                player += 1
                            else:
                                print("Вы не можете подкинуть карту ", player1_move, " на стол")
                                player1_turn = True
                                player2_turn = False
                        elif not self.table_cards:
                            player_input = int(input(f"Игрок {player_number(player)} атакует. Введи индекс карты в руке: "))
                            player1_move = self.player1_hand[player_input - 1]
                            console.print(f"Игрок {player_number(player)} выложил на стол карту: [bold]{player1_move}[/bold]")
                            self.player1_hand.remove(player1_move)
                            self.table_cards.append(player1_move)
                            self.show_table()
                            player1_turn = False
                            player2_turn = True
                            player += 1
                else:
                    if self.table_cards and self.table_cards[-1] and any(card > self.table_cards[-1] for card in self.player2_hand):
                        player_input = int(input(f"Игрок {player_number(player)} отбивается. Введи индекс карты в руке: "))
                        player2_move = self.player2_hand[player_input - 1]
                        if player2_move > player1_move:
                            console.print("Карта ", player1_move, "бита картой", player2_move)
                            self.player2_hand.remove(player2_move)
                            self.table_cards.append(player2_move)
                            self.show_table()
                            player1_turn = True
                            player2_turn = False
                            player += 1
                        else:
                            console.print("Карта не бита, введи номер другой карты (она у тебя точно есть)")
                            player1_turn = False
                    else:
                        print("Игрок ", player_number(player),  " не может побить последнюю карту на столе. Он проигрывает и забирает карты.")
                        self.player2_hand.extend(self.table_cards)
                        self.table_cards = []
                        player1_turn = True
                        player2_turn = False
                        next_round = True
                        player += 1


            self.draw_to_ten(self.player1_hand)
            self.draw_to_ten(self.player2_hand)
            self.player2_hand, self.player1_hand = self.player1_hand, self.player2_hand


if __name__ == "__main__":
    game = CardGame()
    game.play()