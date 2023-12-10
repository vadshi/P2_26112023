# Начнем с создания карты
# ♥ ♦ ♣ ♠
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

    def draw(self, x: int) -> list[Card]:
        # Принцип работы данного метода прописан в 00_task_deck.md
        x *= x > 0  # Добавили проверку того, что x > 0
        drawn_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return drawn_cards

    def shuffle(self):
        random.shuffle(self.cards)


if __name__ == '__main__':
    # # # Создадим несколько карт
    card1 = Card("10", "Hearts")
    card2 = Card("A", "Diamonds")
    card3 = Card("10", "Diamonds")

    # Выведем карты на экран в виде: 10♥ и A♦
    print(card1)
    print(card2)
    print(card3)

    # Проверим, одинаковые ли масти у карт
    if card1.equal_suit(card2):
        print(f"У карт: {card1} и {card2} одинаковые масти")
    else:
        print(f"У карт: {card1} и {card2} разные масти")

    print(card1 > card2)
    print(card1 < card2)
    print(card1 > card3)
    print(card1 < card3)

    # Создаем колоду
    deck = Deck()

    # Выводим колоду
    deck.show()

    # Тасуем колоду
    deck.shuffle()
    print(deck)

    # Возьмем 5 карт "в руку"
    hand = deck.draw(5)

    # Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
    print(deck)

    # Выводим список карт "в руке"(список hand)
    print(f'{hand = }')

    print('Min card:', min(hand))
    print('Max card:', max(hand))
    print('Before sorting:')
    print(f'{hand = }')
    hand.sort()
    print('After sorting:')
    print(f'{hand = }')

    print(deck.cards[-1])
    print(deck.cards[-1].value)
    print(deck.cards[-1].suit)

