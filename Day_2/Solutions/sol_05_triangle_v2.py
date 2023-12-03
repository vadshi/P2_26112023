from __future__ import annotations


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self: Point, other_point: Point) -> float:
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)**(1/2)


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimeter(self):
        return self.p1.distance(self.p2) + self.p2.distance(self.p3) + self.p3.distance(self.p1)

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** (1/2)



# Треугольник задан координатами трех точек
triangle = Triangle(Point(2, 4), Point(6, 8), Point(8, 0))



# Задание:
# найдите площадь и периметр треугольника, реализовав методы area() и perimeter()

print("Периметр треугольника = ", triangle.perimeter())
print("Площадь треугольника = ", triangle.area())