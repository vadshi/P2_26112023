class Rect:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def rotate(self):
        self.width, self.length = self.length, self.width

    def __repr__(self) -> str:
        return f'Rect({self.width}x{self.length})'

    def __str__(self) -> str:
        return f'Прямоугольник(ширина={self.width}, длина={self.length})'

    # 3) r1 * 5 (__mul__()) - обе стороны станут в 5 раз больше
    def __mul__(self, n: int | float):
        if type(n) in (int, float):
            self.width *= n
            self.length *= n
        else:
            raise TypeError("bad type")

    # 4) r1 < r2, r1 == r2, r1 <= r1 и т.п.
    #  меньше '<'
    def __lt__(self, other) -> bool:
        return self.area() < other.area()

    # больше '>'
    def __gt__(self, other) -> bool:
        return self.area() > other.area()

    # меньше или равен '<='
    def __le__(self, other) -> bool:
        return self.area() <= other.area()

    # больше или равен '>='
    def __ge__(self, other) -> bool:
        return self.area() >= other.area()

    # равны '=='
    def __eq__(self, other) -> bool:
        return self.area() == other.area()

    # не равны '!='
    def __ne__(self, other) -> bool:
        return self.area() != other.area()


# Тестовая часть
r1 = Rect(5, 10)
r2 = Rect(6, 7)
print(f"r1 - {r1!s}")
print(f"r2 - {r2!s}")

print("Площадь: ", r1.area())
print("Периметр: ", r1.perimeter())

print("Площадь: ", r2.area())
print("Периметр: ", r2.perimeter())

if r1 == r2:
    print("Прямоугольники равны")
else:
    print("Прямоугольники не равны")

r2 * 10
print(f"r1 - {r1!s}")
print(f"r2 - {r2!s}")

if r1 != r2:
    print("Прямоугольники не равны")
else:
    print("Прямоугольники равны")

if r2 < r1:
    print("r2 меньше r1")
else:
    print("r2 не меньше r1")

if r1 > r2:
    print("r1 больше r2")
else:
    print("r1 не больше r2")

if r2 < r1:
    print("r2 меньше или равен r1")
else:
    print("r2 не меньше и не равен r1")

if r1 > r2:
    print("r1 больше или равен r2")
else:
    print("r1 не больше и не равен r2")

print(r1 == r2)
print(r1 != r2)
print(r1 > r2)
print(r1 >= r2)
print(r1 < r2)
print(r1 <= r2)