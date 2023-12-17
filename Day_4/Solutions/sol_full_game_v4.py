import random

"""
Cоздадим имитацию ходов в “Дурака без козырей”:

1. Создайте колоду из 52 карт. Перемешайте ее.
2. Первый игрок берет сверху 10 карт
3. Второй игрок берет сверху 10 карт.
4. Игрок-1 ходит:
    4.1. игрок-1 выкладывает самую маленькую карту по "старшенству"
    4.2. игрок-2 пытается бить карту, если у него есть такая же масть, но значением больше.
    4.3. Если игрок-2 не может побить карту, то он проигрывает/забирает себе(см. пункт 7)
    4.4. Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
5. Если Игрок-2 отбился, то Игрок-1 и Игрок-2 меняются местами. Игрок-2 ходит, Игрок-1 отбивается.
6. Выведите в консоль максимально наглядную визуализацию данных ходов (библиотека rich)
7* Реализовать возможность добрать карты из колоды после того, как один из игроков отбился/взял в руку
"""

VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = { # ♠<♣<♦<♥
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
        return str(self) # внешняя функция str которая обращается к дандер-методу self.__str__()

    def equal_suit(self, other_card) -> bool:
        return self.suit == other_card.suit

    def __gt__(self, other_card) -> bool:
        if self.value == other_card.value:
            return SUITS.index(self.suit) > SUITS.index(other_card.suit)
        return VALUES.index(self.value) > VALUES.index(other_card.value)

    def __lt__(self, other_card) -> bool:
        # Можно и так, но пока лучше все прописывать
        # return not self.more(other_card)
        if self.value == other_card.value:
            return SUITS.index(self.suit) < SUITS.index(other_card.suit)
        return VALUES.index(self.value) < VALUES.index(other_card.value)


class Deck:
    def __init__(self, deck_size = 52):
        self.cards = []
        self.size = int(len(VALUES) - (deck_size / 4))
        for suit in SUITS:
            for val in VALUES[self.size:]:
                self.cards.append(Card(val, suit))

    def __str__(self):
        out_cards = []
        for card in self.cards:
            out_cards.append(str(card))
        return f'Колода[{len(self.cards)}]: {", ".join(out_cards)}'

    def draw(self, x: int) -> list:
        x *= x > 0  # добавили проверку того, что x > 0  # БЕЗ ИСПОЛЬЗОВАНИЯ IF...
        take_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return take_cards

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self, fullhand, name='Игрок'):
        self.cards = []
        self.name = name
        self.fullhand = fullhand
    
    def __str__(self):
        out_cards = []
        for card in self.cards:
            out_cards.append(str(card))
        return f'{self.name}[{len(self.cards)}]: {", ".join(out_cards)}'

    def fill(self, deck):  # пополнить руку 
        need_cards = self.fullhand - len(self.cards)
        if need_cards > 0:
            free_cards = len(deck.cards)
            if free_cards >= need_cards:
                self.cards += deck.draw(need_cards)
            else:
                self.cards += deck.draw(free_cards)  # deck.draw не может принимать 0 или значение < 0


class Round:
    def __init__(self, striker: Player, defender: Player, deck):
        self.pairs = []  # pairs = [[3♥, 5♥], [5♣]]
        self.striker = striker
        self.defender = defender
        self.deck = deck

    def __str__(self):
        out_pairs = []
        for pair in self.pairs:
            out_pairs.append(str(pair))
        return f'round: {", ".join(out_pairs)}'

    def show(self):
        out_pairs = []
        for pair in self.pairs:
            out_pairs.append(str(pair))
        return f'Итог раунда: {", ".join(out_pairs)}'

    def init_round(self):  # инициализация раунда (добавляется первая атакующая карта)
        if len(self.pairs) == 0:
            min_card_id = self.striker.cards.index(min(self.striker.cards))
            self.pairs.append([self.striker.cards.pop(min_card_id),]) 

    def take_from_table(self):
        for pair in self.pairs:
            while pair:
                self.defender.cards.append(pair.pop())
        self.pairs.clear()

    def get_protect_card(self, attack_card) -> Card | None:
        self.defender.cards.sort()
        for defend_card in self.defender.cards:
            if defend_card > attack_card and defend_card.suit == attack_card.suit:
                protect_card_id = self.defender.cards.index(defend_card)
                return self.defender.cards.pop(protect_card_id)

    def get_attack_card(self, some_card: Card) -> Card:
        for pair in self.pairs:
            for strike_card_id, strike_card in enumerate(self.striker.cards):
                if some_card.value == strike_card.value:
                    return self.striker.cards.pop(strike_card_id)


    def play(self):
        
        self.init_round()

        while True:
            if len(self.pairs[-1]) == 1:  # защищайся
                attack_card = self.pairs[-1][0]
                protect_card = self.get_protect_card(attack_card)
                if protect_card:
                    self.pairs[-1].append(protect_card) # дополни пару (успешная защита)
                    continue
                else:
                    print(f"{self.show()} -> {self.defender.name} забрал")
                    self.take_from_table() # возьми со стола (нет карт для защиты)
                    self.striker.fill(self.deck)
                    print(self.striker)
                    print(self.defender)
                    print(self.deck)
                    return False
            elif len(self.pairs[-1]) == 2 and not self.defender.cards: # если у защитника кончились карты - он победил
                print(f"{self.show()} -> {self.defender.name} ОТБИЛСЯ И ПОБЕДИЛ !!!!!!!!!!!!!!!!!!!")
                self.pairs.clear() # бита удаляется
                print(self.striker)
                print(self.defender)
                print(self.deck)
                return True
            elif len(self.pairs[-1]) == 2: # нападай
                breaker = False
                attack_card = None
                for pair in self.pairs:
                    if breaker:
                        break
                    for card in pair:
                        attack_card = self.get_attack_card(card)
                        if attack_card:
                            self.pairs.append([attack_card,])
                            breaker = True
                            break
                if attack_card is None:
                    print(f"{self.show()} -> Бита и переход хода")
                    self.pairs.clear() # бита удаляется
                    self.striker.fill(self.deck)
                    self.defender.fill(self.deck)
                    print(self.striker)
                    print(self.defender)
                    print(self.deck)
                    return True


class Game:
    def __init__(self, deck_size = 20, fullhand = 6):
        self.deck = Deck(deck_size)
        self.deck.shuffle()
        self.player1 = Player(fullhand, "Игрок_1")
        self.player2 = Player(fullhand, "Игрок_2")
       
    def __str__(self):
        pass

    def run(self):
        print("\nРаздача карт перед началом игры:")
        print(self.deck)

        self.player1.fill(self.deck)
        self.player2.fill(self.deck) 

        print(self.player1)
        print(self.player2)
        print(self.deck)
        
        striker = self.player1
        defender = self.player2

        while striker.cards and defender.cards:
            print(f"====================Ходит {striker.name}====================")
            round = Round(striker, defender, self.deck)
            change = round.play()
            if change:
                striker, defender = defender, striker


game = Game()
game.run()

