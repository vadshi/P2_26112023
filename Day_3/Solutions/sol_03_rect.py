"""
Прямоугольник по двум сторонам.
Создать класс прямоугольник:

а) при создании указывается ширина и длина

r = Rect(5, 10)

б) методы для площади и периметра

print(r.area())       # возвращает площадь
print(r.perimeter())  # периметр

в) масштабирование и поворот
от 1 до infinity увеличение в n, от 0 до 1 - уменьшение в n раз
r.scale(10) - ширина и длина увеличиваются в 10 раз
r.scale(0.1) - ширина и длина уменьшаются в 10 раз
r.rotate() - меняется местами ширина и длина

г) перегрузить магические методы __repr__ и __str__
"""
import random


class Rect:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def scale(self, n: int | float):
        self.width *= n
        self.length *= n

    def rotate(self):
        self.width, self.length = self.length, self.width

    def __repr__(self) -> str:  # repr()
        return f'Rect({self.width}x{self.length})'

    def __str__(self) -> str:  # str()
        return f'Прямоугольник(ширина={self.width}, длина={self.length})'


# Тестовая часть
rect = Rect(5, 10)
print("Площадь: ", rect.area())
print("Периметр: ", rect.perimeter())

if random.randint(0, 1):
    rect.scale(10)
    # Покажи значение rect, используя метод __str__()
    print(f"Увеличение: {rect!s}")
else:
    rect.scale(0.1)
    print(f"Уменьшение: {rect!s}")


print("Площадь: ", rect.area())
print("Периметр: ", rect.perimeter())
print(rect)
print(repr(rect))
print("Before rotate: ", rect)
rect.rotate()
print("After rotate: ", rect)
