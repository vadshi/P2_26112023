import time

from rich.console import Console
from rich.table import Table
from rich import box
import random

from rich.text import Text

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
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit    # Масть карты

    def __str__(self):
        return self.value + SUITS_UNI[self.suit]

    def __repr__(self):
        return str(self)  # self.__str__()

    def equal_suit(self, other_card) -> bool:
        return self.suit == other_card.suit

    def __gt__(self, other_card) -> bool:  # >
        if self.value == other_card.value:
            return SUITS.index(self.suit) > SUITS.index(other_card.suit)
        return VALUES.index(self.value) > VALUES.index(other_card.value)

    def __lt__(self, other_card) -> bool:  # <
        # Можно и так, но пока лучше все прописывать
        # return not self > other_card)
        if self.value == other_card.value:
            return SUITS.index(self.suit) < SUITS.index(other_card.suit)
        return VALUES.index(self.value) < VALUES.index(other_card.value)


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(value, suit))

    def __str__(self):
        return f"deck[{len(self.cards)}] {', '.join([str(card) for card in self.cards])}"

    def __repr__(self):
        return str(self)

    def show(self) -> None:
        # Принцип работы данного метода прописан в 00_task_deck.md
        print(f'deck[{len(self.cards)}]', end=' ')
        print(*self.cards, sep=', ')

    def draw(self, x: int):
        # Принцип работы данного метода прописан в 00_task_deck.md
        x *= x > 0  # Добавили проверку того, что x > 0
        drawn_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return drawn_cards

    def shuffle(self):
        random.shuffle(self.cards)





""" РЕШЕНИЕ """

console = Console()
deck = Deck()
deck.shuffle()


def display_game_state(player1, player2, cards_on_table):
    #console.clear()
    console.print(f'{player1.name}:  {player1.hand}\n'
                  f'{player2.name}: {player2.hand}\n'
                  'Table: ' + str(cards_on_table))


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def min_card(self):
        if not self.hand:
            return None
        min_card = min(self.hand)
        self.hand.remove(min_card)
        return min_card

    def beating_card(self, played_card: Card) -> Card | None:
        for card in self.hand:
            if card.suit == played_card.suit and card > played_card:
                console.print(f'Игрок {self.name} бъет карту {played_card} своей картой {card}')
                self.hand.remove(card)
                return card

    def toss_card(self, cards_on_table: list[Card]) -> Card | None:
        for card in self.hand:
            for card_t in cards_on_table:
                if card.value == card_t.value:
                    self.hand.remove(card)
                    return card

    def draw_cards(self, deck, num_cards):  # добор карт
        while len(self.hand) < num_cards:
            new_card = deck.draw(1)
            if new_card:
                self.hand.extend(new_card)


player1 = Player("Ваня")
player1.hand = deck.draw(10)

player2 = Player("Петя")
player2.hand = deck.draw(10)

players = [player1, player2]
cards_on_table = []
new_round = True

while player1.hand and player2.hand:

    if new_round:
        print('=' * 42)

        console.print(f'Игроки добирают карты...')
        for player in players:
            if len(deck.cards) > 0:
                player.draw_cards(deck, 10)
        console.print(f'В колоде осталось {len(deck.cards)} карт')

        console.print(f'Играет: {players[0].name}')
        played_card = players[0].min_card()
        cards_on_table.append(played_card)
        display_game_state(players[0], players[1], cards_on_table)

    beating_card = players[1].beating_card(played_card)
    if beating_card is not None:
        cards_on_table.append(beating_card)
        toss_card = players[0].toss_card(cards_on_table)
        if toss_card:
            console.print(f'{players[0].name} подбрасывает {toss_card}')
            cards_on_table.append(toss_card)
            played_card = toss_card
            console.print(f'Table: {cards_on_table}')
            new_round = False
        else:
            console.print(f'{players[0].name} Не знает что подбросить. Переход хода')
            cards_on_table = []
            players.reverse()
            new_round = True

    else:
        console.print(f'{players[1].name} не смог побиться. Забирает все')
        players[1].hand = players[1].hand + cards_on_table
        cards_on_table = []
        new_round = True



if not player1.hand:
    console.print(f"Игрок {player1.name} выиграл!")
elif not player2.hand:
    console.print(f"Игрок {player2.name} выиграл!")
else:
    console.print(f"Ничья.")
