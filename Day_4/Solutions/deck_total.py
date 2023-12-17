import random

VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
    'Spades': '♠',
    'Clubs': '♣',
    'Diamonds': '♦',
    'Hearts': '♥'
}


class Card:
    def __init__(self, value, suit):
        self.value = value; self.suit = suit

    def to_str(self):
        return self.value + SUITS_UNI[self.suit]

    def __str__(self):
        return self.value + SUITS_UNI[self.suit]

    def __repr__(self):
        return self.value + SUITS_UNI[self.suit]

    def equal_suit(self, other_card) -> bool:
        return self.suit == other_card.suit

    def more(self, other_card) -> bool:
        if self.value == other_card.value:
            return SUITS.index(self.suit) > SUITS.index(other_card.suit)
        return VALUES.index(self.value) > VALUES.index(other_card.value)

    def less(self, other_card) -> bool:
        if self.value == other_card.value:
            return SUITS.index(self.suit) < SUITS.index(other_card.suit)
        return VALUES.index(self.value) < VALUES.index(other_card.value)


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(value, suit))

    def __str__(self):
        return f"deck[{len(self.cards)}] {', '.join([str(card.to_str()) for card in self.cards])}"

    def __repr__(self):
        return str(self)

    def draw(self, x: int) -> list[Card]:
        x *= x > 0
        drawn_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return drawn_cards

    def shuffle(self):
        random.shuffle(self.cards)


# дополнительные функции
# показывает карты в "руках" у игрока
def show(hand):
    print(f"{', '.join([card.to_str() for card in hand])}")


# сортирует карты по возрастанию
def sort(hand):
    return hand.sort(key=lambda x: VALUES.index(x.value))


if __name__ == '__main__':
    # Создаем колоду
    deck = Deck()
    # Выводим колоду
    print(deck)
    # Тасуем колоду
    deck.shuffle()

    print(deck)
    # Возьмем 5 карт "в руку"
    hand = deck.draw(5)
    # Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
    print(deck)
    # Выводим список карт "в руке"(список hand)
    show(hand)
    # "добирает" необходимое количество карт из колоды
    hand += deck.draw(10 - len(hand))
    # Выводим список карт "в руке"(список hand)


    sort(hand)
    show(hand)
    print(hand)

    hand.remove(hand[0])

    for card in hand:
        print(card.to_str())
