# from deck_total import Card, Deck

'''
создадим имитацию ходов в “Дурака без козырей”:

1. Создайте колоду из 52 карт. Перемешайте ее.
2. Первый игрок берет сверху 10 карт
3. Второй игрок берет сверху 10 карт.
4. Игрок-1 ходит:
    4.1. игрок-1 выкладывает самую маленькую карту по значению
    4.2. игрок-2 пытается бить карту, если у него есть такая же масть, но значением больше.
    4.3. Если игрок-2 не может побить карту, то он проигрывает/забирает себе(см. пункт 7)
    4.4. Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
5. Если Игрок-2 отбился, то Игрок-1 и Игрок-2 меняются местами. Игрок-2 ходит, Игрок-1 отбивается.
6. Выведите в консоль максимально наглядную визуализацию данных ходов.
7* Реализовать возможность добрать карты из колоды после того, как один из игроков отбился/взял в руку
'''
import random
from rich.console import Console
from rich.table import Table

# Начнем с создания карты
# ♥ ♦ ♣ ♠
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
    'Spades': '♠',  # пики
    'Clubs': '♣',  # трефы
    'Diamonds': '♦',  # бубна
    'Hearts': '♥'  # червы
}


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __str__(self):
        return self.value + ' ' + SUITS_UNI[self.suit]

    def __repr__(self):
        return str(self)

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gt__(self, other_card):
        res = VALUES.index(self.value) > VALUES.index(other_card.value)
        if VALUES.index(self.value) == VALUES.index(other_card.value):
            res = SUITS.index(self.suit) > SUITS.index(other_card.suit)
        return res

    def __lt__(self, other_card):
        res = VALUES.index(self.value) < VALUES.index(other_card.value)
        if VALUES.index(self.value) == VALUES.index(other_card.value):
            res = SUITS.index(self.suit) < SUITS.index(other_card.suit)
        return res


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = [Card(v, s) for s in SUITS for v in VALUES]

    def show(self):
        '''
        метод .**show**() - отображает все карты колоды в формате: \
         deck[12]: 3♥, 4♦, A♣, … \
          где 12 - текущее кол-во карт в колоде.
        '''
        return f'desk[{len(self.cards)}]{self.cards}'

    def draw(self, x: int) -> list[Card]:
        '''
        *   метод .**draw**(x) - возвращает x первых карт из колоды в виде списка, эти карты **убираются** из колоды.
         Уточнение: первую карту в списке считаем верхней картой колоды
        '''
        res = []
        if x > 0 and len(self.cards) > 0:
            res = self.cards[:x]
            del self.cards[:x]
        return res

    def shuffle(self):
        # Обратите внимание на: https://www.w3schools.com/python/ref_random_shuffle.asp
        random.shuffle(self.cards)


class Player:
    def __init__(self, name: str):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        self.name = name
        # в текущих условиях задачи алгоритм зацикливается, если есть карта, минимальная для обоих игроков, и не может побиться ни одним из игроков и карты в колоде закончились
        # поэтому запомним минимальную ошибочную карту, и если они совпадают у обоих игроков и карты на доске закончились, то игра останавливается
        self.failcard = None

    def remove_card(self, card: Card):
        # удаляем карту у игрока
        self.cards.remove(card)

    def take_cards(self, cards: list):
        # грок добавляет карты к себе
        self.cards += cards

    def put_mincard(self):
        return min(self.cards)

    def put_othercard_values(self, cards: list) -> Card | None:
        """ Возвращает карту того же значения, что карты на столе """
        card = None
        t_cards = []
        t_values = [c.value for c in cards]  # список значений карт на столе
        for c in self.cards:
            if c.value in t_values:
                t_cards += [c]
        if len(t_cards):
            card = random.choice(t_cards)
        return card

    def cover_card(self, card: Card):
        # Находим карту такой же масти как у card, но значением больше.
        i = 0
        res = None
        while i < len(self.cards):
            if card.suit == self.cards[i].suit and self.cards[i] > card:
                res = self.cards[i]
                break
            i += 1
        return res

    def show_cards(self):
        # показываем карты у игрока
        return f'Player {self.name} [{len(self.cards)}] {self.cards}'


class Game:
    def __init__(self, table: Table, deck: Deck, pl1: Player, pl2: Player, max_step: int = 100):
        self.table = table
        self.deck = deck
        self.pl1 = pl1
        self.pl2 = pl2
        self.step = 1
        self.max_step = max_step

        self.table.add_column("Player1")
        self.table.add_column("Deck")
        self.table.add_column("Player2")

    def go_on(self) -> bool:
        # условие окончания игры
        # ни у одного игрока не окончились карты и мы не превысили максимальное количество шагов и
        # в текущих условиях алгоритм зацикливается, если карты на столе закончились, и карта минимальная для обоих игроков и они не могут оба ее отбить
        # они будут просто передавать ее друг другу и он будет выпадать каждый раз как минимальная карта, а второй не сможет ее отбить
        # проверяем это условия и останавливаем игру если ошибочные карты совпадают у игроков и карты на доске закончились
        return (len(self.pl1.cards) and len(self.pl2.cards) and self.step <= self.max_step) and \
            (len(self.deck.cards) or ((self.pl1.failcard is None or self.pl2.failcard is None or self.pl1.failcard != self.pl2.failcard) and len(
                self.deck.cards) == 0))

    def show_players_cards(self):
        # показываем карты игроков
        self.table.add_row(self.pl1.show_cards(), ' ', self.pl2.show_cards())

    def increase_step(self):
        self.step += 1

    def player_take_cards(self, p: Player, nc: int):
        if len(self.deck.cards) > 0:
            p.take_cards(self.deck.draw(nc))  # игрок добирает nc карт с доски

    def first_step(self):
        # первый игрок бросает минимальную карты
        c1 = min(self.pl1.cards)  # self.pl1.put_mincard()
        self.pl1.remove_card(c1)  # карта уходит от первого игрока
        c2 = self.pl2.cover_card(c1)  # второй игрок пытается ее побить
        if c2 is None:  # второй игрок не смог отбить первую карту
            self.pl2.take_cards([c1])  # второй игрок забирает карту
            self.pl2.failcard = c1  # запоминаем минимальную карту которую он не смог побить
            self.player_take_cards(self.pl1, 1)  # первый игрок добирает одну карту с доски
            self.table.add_row(' ', str(c1) + 'Нет Карты', f'Player [{self.pl2.name}] Fail')
        else:
            # если на первом шаге второй игрок отбился от первой карты
            self.table.add_row(' ', str(c1) + str(c2), f'Player [{self.pl2.name}] Win')
            self.pl2.remove_card(c2)  # карта уходит от второго игрока
        return [c2 is not None, c1, c2]

    def second_step(self, c1: Card, c2: Card):
        # зацикливаем, первый игрок бросает карты того же значения, что и на столе, пока они у него есть
        deck_cards = [c1, c2]  # массив карт на столе которые бросают игроки, заполняем картами после первого шага
        take_kards = False  # оба игрока набирают карты с колоды
        while self.go_on():
            c3 = self.pl1.put_othercard_values(deck_cards)  # первый игрок выбирает любую карты в колоде первого игрока с теми же значениями, что карты на столе
            if c3 is not None:  # есть такая карта, играем, иначе выходим
                deck_cards += [c3]  # карта упала на стол
                self.pl1.remove_card(c3)
                c4 = self.pl2.cover_card(c3)  # второй игрок пытается отбить вторую карту
                if c4 is None:  # второй игрок не отбил вторую карту,
                    self.pl2.take_cards(deck_cards)  # второй игрок забирает все карты
                    self.player_take_cards(self.pl1, int((len(deck_cards) - 1) / 2) + 1)  # первый игрок берет столько карт, сколько скинул (можно поменят на условие, что берут до 10, если больше 10 то не берут)
                    self.table.add_row(' ', str(c3) + 'Нет Карты', f'Player [{self.pl2.name}] Fail')
                    take_kards = False
                    break
                else:  # второй игрок отбил вторую карту
                    deck_cards += [c4]  # добавляем карту второго игрока на стол
                    self.table.add_row(' ', str(c3) + str(c4), f'Player [{self.pl2.name}] Win')
                    self.pl2.remove_card(c4)
                    take_kards = True
            else:
                take_kards = True
                break
        if take_kards:  # если второй игрок отбился, то
            # оба игрока добирают столько карт, сколько скинули с учетом первого шага(можно поменят на условие, что берут до 10, если больше 10 то не берут)
            self.player_take_cards(self.pl1, int(len(deck_cards) / 2))  # берут столько карт, сколько скинули в игре
            self.player_take_cards(self.pl2, int(len(deck_cards) / 2))
            return True
        return False

    def playing(self):
        res_step1 = self.first_step()  # вовращаем результат первого шака и карты с первого шага
        if res_step1[0]:  # если на первом шаге второй игрок отбился от первой карты
            # переходим ко второму шагу
            return self.second_step(res_step1[1], res_step1[2])
        return False

    def finish(self):
        print()
        print('------Окончание игры--------')
        print(self.pl1.show_cards())
        print(self.pl2.show_cards())
        print(f'Количество ходов: {self.step - 1}')
        if len(self.pl1.cards) < len(self.pl2.cards):
            print(f'Player {self.pl1.name} Win!')
        elif len(self.pl1.cards) == len(self.pl2.cards):
            print('Победила дружба!')
        else:
            print(f'Player {self.pl2.name} Win!')

    def change_places(self):
        self.pl1, self.pl2 = self.pl2, self.pl1  # меняемся местами


# ----------------------------------------full_game----------------------------------------
def main():
    n_start = 10  # сколько карт берут игроки
    max_step = 100  # максимальное количество шагов в игре
    d = Deck()
    table = Table(title="Игра в дурака")
    table_d = Table()
    console = Console()
    table_d.add_column('Карты на доске')
    p1 = Player('Ivan')
    p2 = Player('Serj')

    game = Game(table, d, p1, p2, max_step)
    # game.deal_cards(n_start) #сдаем карты
    d.shuffle()  # мешаем карты
    table_d.add_row(d.show())
    # игроки берут по n_start карты
    p1.take_cards(d.draw(n_start))
    p2.take_cards(d.draw(n_start))

    console.print(table_d)  # показываем карты на доске

    while game.go_on():
        # print(f'Ход {game.step} {game.pl1.name}')
        game.table.add_row('', f'Ход {game.step} {game.pl1.name}', '')
        game.show_players_cards()  # показываем карты игроков перед ходом
        res = game.playing()  # играем
        if res:
            game.change_places()  # игроки меняются местами
        game.increase_step()  # можно написать game.step+=1
        game.table.add_row('-' * 20, '-' * 10, '-' * 20)

    console.print(table)
    game.finish()


if __name__ == '__main__':
    main()
