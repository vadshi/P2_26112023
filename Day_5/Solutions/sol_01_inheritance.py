"""
## 2.1 Квадрат
сделать класс Square - квадрат, который наследуется от прямоугольника

Класс Point(x: int, y: int)

# прямоугольник создаем на основе двух точек (class Point)
Класс Rect(p1, p2)

rect = Rect(p1: Point, p2: Point)
p1 = left_bottom -> (1, 1)  # левая нижняя
p2 = right_top -> (4, 5)    # правая верхняя
methods: area, perimeter (можно через property), __repr__, __str__


class Square(Rect):
    def __init__(self, p1, size):
        # ...

    # добавить метод вычисления диагонали
    def diagonal():
        pass
    
sq = Square(p1, 5)  # Квадрат 5x5
print(sq.area())
print(sq.perimeter())
print(sq.diagonal())
print(sq)
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rect:
    def __init__(self, p1, p2):
        self.a = p2.x - p1.x
        self.b = p2.y - p1.y

    def __str__(self):
        return f'{self.__class__.__name__}({self.a}x{self.b})'

    def __repr__(self):
        return str(self)

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Square(Rect):
    def __init__(self, p1, size):
        p2 = Point(p1.x + size, p1.y + size)
        Rect.__init__(self, p1, p2)
        self.size = size

    def diagonal(self):
        return self.size * 2 ** 0.5


point1 = Point(1, 1)
point2 = Point(4, 5)
rect = Rect(point1, point2)
print(rect)
print(rect.area())
print(rect.perimeter())

sq = Square(point1, 5)  # Квадрат 5x5
print(sq)
print(sq.area())
print(sq.perimeter())
print(sq.diagonal())
