import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """  Подбрасывание монетки """
        self.side = random.choice(['heads', 'tails'])
        # return side # Это ошибка, здесь return не нужен


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# не выпала ни орлом ни решкой. Монетка "определяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())


n = int(input('Введите количество монет: '))
# 1. Создаем список из n монет.
coins = []
for _ in range(n):
    coin = Coin()
    coins.append(coin)

# 2. Подкидываем все монетки
for coin in coins:
    coin.flip()

# 3. Считаем количество орлов и решек.
heads = tails = 0
for coin in coins:
    if coin.side == 'heads':
        heads += 1
    elif coin.side == "tails":
        tails += 1

# 4. Выводим процентное соотношение орлов и решек
print(f'Орлы: {heads / n:.2%}')
print(f'Решки: {tails / n:.2%}')
