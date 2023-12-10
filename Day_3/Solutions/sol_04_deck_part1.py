import random
from sol_card_deck import Card, VALUES, SUITS


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
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
print(hand)
