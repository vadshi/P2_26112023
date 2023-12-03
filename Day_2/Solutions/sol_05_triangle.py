from __future__ import annotations


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self: Point, other_point: Point) -> float:
        return round(((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5, 2)


class Triangle:
    def __init__(self, p1, p2, p3):
        self.a = p1.distance(p2)
        self.b = p2.distance(p3)
        self.c = p1.distance(p3)

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        per = self.perimeter() / 2
        return round((per * (per - self.a) * (per - self.b) * (per - self.c)) ** 0.5, 2)


# Треугольник задан координатами трех точек
triangle = Triangle(Point(2, 4), Point(6, 8), Point(8, 0))

# Задание:
# найдите площадь и периметр треугольника, реализовав методы area() и perimeter()

print("Периметр треугольника = ", triangle.perimeter())
print("Площадь треугольника = ", triangle.area())