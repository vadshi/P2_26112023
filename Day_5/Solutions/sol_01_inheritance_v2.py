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

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Rect:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    @property
    def side_a(self):
        return self.p2.x - self.p1.x

    @property
    def side_b(self):
        return self.p2.y - self.p1.y

    def area(self):
        return self.side_a * self.side_b

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def __str__(self):
        return f'{self.__class__.__name__}({self.side_a}x{self.side_b})'


class Square(Rect):
    def __init__(self, p1, size):
        p2 = Point(p1.x + size, p1.y + size)
        Rect.__init__(self, p1, p2)

    def diagonal(self):
        return self.p1.distance(self.p2)


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
print("Сторона квадрата:", sq.side_a)
