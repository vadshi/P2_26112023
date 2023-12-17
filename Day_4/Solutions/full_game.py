# Cоздадим имитацию ходов в “Дурака без козырей”:
from deck_total import Card, Deck, show, sort
import time

# 1. Создайте колоду из 52 карт. Перемешайте ее.
# Создаем колоду
deck = Deck()
# Тасуем колоду
deck.shuffle()
# Смотрим что получилось
print(deck)
# 2. Первый игрок берет сверху 10 карт
hand_1 = deck.draw(10)
sort(hand_1)
print ("У игрока 1 на руках:")
show(hand_1)
# 3. Второй игрок берет сверху 10 карт.
hand_2 = deck.draw(10)
sort(hand_2)
print ("У игрока 2 на руках:")
show(hand_2)

# Игра 
table = [] # Игровой стол
aktiv_player = 1  # Начинает 1 игрок
beaten = 0  # Индикатор ситуации на игровом столе "0" - игра продолжается, "1" - карта отбита, "2" - не смог отбиться

# пока у игроков есть карты на руках - игра продолжается
while len(hand_1) > 0 and len(hand_2) > 0:
    if aktiv_player == 1:  # если заходит 1 ирок
        #  пока у 1 игрока есть карты и не победил 2 игрок
        while len(hand_1) > 0 and len(hand_2) > 0 and aktiv_player == 1:
            beaten = 2
            # 4.1. игрок-1 выкладывает самую маленькую карту по "старшенству" 
            if len(table) == 0:
                table.insert(0, hand_1[0])
                print("Игрок 1 пошел: ", table[0].to_str(), end=' <-> ')
                del hand_1[0]
                time.sleep(0)
            # 4.2. игрок-2 пытается бить карту, если у него есть такая же масть, но значением больше.
            for i in hand_2:
                if table[0].equal_suit(i) and i.more(table[0]):
                    table.append(i)
                    beaten = 1  # карта бита
                    print(i.to_str(), " - Игрок 2 отбил  ")
                    time.sleep(0)
                    hand_2.remove(i)
                    break
                    # 4.3. Если игрок-2 не может побить карту, то он проигрывает/забирает себе
            if beaten == 2:
                print("Игроку 2 нечем отбиться, забирает карты")
                time.sleep(0)
                hand_2.extend(table)
                table.clear()
                hand_1 += deck.draw(10 - len(hand_1))
                sort(hand_1)
                print ("У игрока 1 на руках:")
                show(hand_1)
                hand_2 += deck.draw(10 - len(hand_2))
                sort(hand_2)
                print ("У игрока 2 на руках:")
                show(hand_2)
                
            # 4.4. Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе. 
            if beaten == 1:
                for k in table:
                    for i in hand_1:
                        if k.value == i.value:
                            table.insert(0, i)
                            print("Игрок 1 пошел: ", table[0].to_str(), end=' <-> ')
                            time.sleep(0)
                            hand_1.remove(i)
                            beaten = 2  # продолжаем
                            break
                    if beaten == 2:
                        break
            #  5. Если Игрок-2 отбился, то Игрок-1 и Игрок-2 меняются местами. Игрок-2 ходит, Игрок-1 отбивается.
            if beaten == 1 or len(hand_1) == 0 or len(hand_2) == 0:
                aktiv_player = 2  # переход хода ко 2 игроку
                print("Все карты биты! Переход хода к Игроку 2")
                print("")
                time.sleep(0)
                hand_1 += deck.draw(10 - len(hand_1))
                sort(hand_1)
                print ("У игрока 1 на руках:")
                show(hand_1)
                hand_2 += deck.draw(10 - len(hand_2))
                sort(hand_2)
                print ("У игрока 2 на руках:")
                show(hand_2)

    if aktiv_player == 2:  # если заходит 2 ирок
        # пока у 2 игрока есть карты и не победил 1 игрок
        while len(hand_1) > 0 and len(hand_2) > 0 and aktiv_player == 2:
            beaten = 2
            # 4.1. игрок-2 выкладывает самую маленькую карту по "старшенству" 
            if len(table) == 0:
                table.insert(0, hand_2[0])
                print("Игрок 2 пошел: ", table[0].to_str(), end=' <-> ')
                time.sleep(0)
                del hand_2[0]
            # 4.2. игрок-1 пытается бить карту, если у него есть такая же масть, но значением больше.
            for i in hand_1:
                if table[0].equal_suit(i) is True and i.more(table[0]) is True:
                    table.append(i)
                    beaten = 1  # карта бита
                    print(i.to_str(), " - Игрок 1 отбил")
                    time.sleep(0)
                    hand_1.remove(i)
                    break
            # 4.3. Если игрок-1 не может побить карту, то он проигрывает/забирает себе
            if beaten == 2:
                print("Игроку 1 нечем отбиваться, забирает карты")
                time.sleep(0)
                hand_1.extend(table)
                table.clear()
                hand_1 += deck.draw(10 - len(hand_1))
                sort(hand_1)
                print ("У игрока 1 на руках:")
                show(hand_1)
                hand_2 += deck.draw(10 - len(hand_2))
                sort(hand_2)
                print ("У игрока 2 на руках:")
                show(hand_2)
                
            # 4.4. Если Игрок-1 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе. 
            if beaten == 1:
                for k in table:
                    for i in hand_2:
                        if k.value == i.value:
                            table.insert(0, i)
                            print("Игрок 2 пошел: ", table[0].to_str(), end=' <-> ')
                            time.sleep(0)
                            hand_2.remove(i)
                            beaten = 2  # продолжаем
                            break
                    if beaten == 2:
                        break
            # 5. Если Игрок-1 отбился, то Игрок-2 и Игрок-1 меняются местами. Игрок-2 ходит, Игрок-1 отбивается.
            if beaten == 1 or len(hand_1) == 0 or len(hand_2) == 0:
                aktiv_player = 1  # переход хода ко 1 игроку
                print("Все карты биты! Переход хода к Игроку 1")
                print("")
                time.sleep(0)
                table.clear()
                hand_1 += deck.draw(10 - len(hand_1))
                sort(hand_1)
                print ("У игрока 1 на руках:")
                show(hand_1)
                hand_2 += deck.draw(10 - len(hand_2))
                sort(hand_2)
                print ("У игрока 2 на руках:")
                show(hand_2)

print("---------------------------")
if len(hand_1) == 0 and len(hand_2) > 0:
    print("Победил Игрок 1")
elif len(hand_2) == 0 and len(hand_1) > 0:
    print("Победил Игрок 2")
else:
    print("Боевая ничья!")
print("---------------------------")