""" Реализация игры "Камень, ножницы, бумага" """
import random


class Thing(object):
    def __str__(self):
        return f'{self.__class__.__name__}'


class Rock(Thing):
    pass


class BrownRock(Rock):
    pass


class Paper(Thing):
    pass


class WhitePaper(Paper):
    pass


class Scissors(Thing):
    pass


def beats(x, y):
    if isinstance(x, Rock):
        if isinstance(y, Rock):
            return None  # Нет победителя
        elif isinstance(y, Paper):
            return y
        elif isinstance(y, Scissors):
            return x
        else:
            raise TypeError("Unknown second thing")
    elif isinstance(x, Paper):
        if isinstance(y, Rock):
            return x
        elif isinstance(y, Paper):
            return None  # Нет победителя
        elif isinstance(y, Scissors):
            return y
        else:
            raise TypeError("Unknown second thing")
    elif isinstance(x, Scissors):
        if isinstance(y, Rock):
            return y
        elif isinstance(y, Paper):
            return x
        elif isinstance(y, Scissors):
            return None  # Нет победителя
        else:
            raise TypeError("Unknown second thing")
    else:
        raise TypeError("Unknown first thing")


b_rock, w_paper, scissors = BrownRock(), WhitePaper(), Scissors()
lst = [b_rock, w_paper, scissors, Rock(), Paper()]

# for _ in range(10):
#     first = random.choice(lst)
#     second = random.choice(lst)
#     print(f'{first} vs {second}. {beats(first, second)} win')


# beats(w_paper, 3)  # TypeError: Unknown second thing

# print(type(w_paper) == Paper)       # False
# print(isinstance(w_paper, Paper))   # True
#
# # Пробегаемся по всем классам предкам
# print(isinstance(b_rock, Thing))
# print(isinstance(True, int))
#
# # Показать иерархию классов
# print(b_rock.__class__.__mro__)
# print(True.__class__.__mro__)
#
# # проверяем, что Thing предок класса Rock
# print(issubclass(BrownRock, Thing))  # True
# print(issubclass(Rock, object))      # True
# print(issubclass(Rock, Scissors))    # False
#
# # аргументы - только классы, поэтому ошибка
# print(issubclass(b_rock, Thing))  # Error


