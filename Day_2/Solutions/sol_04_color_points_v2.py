import math

class Point:
    def __init__(self, x, y, color="white"):
        self.x = x
        self.y = y
        self.color = color

    def distance(self, other_point) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# пример работы метода
# p1 = Point(4, 4)
# p2 = Point(3, 3)
#
# result = p1.distance(p2)
# print(result)

# Вычисляем площадь треугольника для каждой группы
def calc_area(point1: Point, point2: Point, point3: Point):
    a = point1.distance(point2)
    b = point2.distance(point3)
    c = point3.distance(point1)
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area


# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно, что точек каждого цвета ровно три,
# но порядок точек в списке произвольный
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]
# Все точки одного цвета соединены линиями и образуют треугольник

# Задание-1: доработайте конструктор class Point для хранения цвета точки
# Задание-2: реализуйте метод distance()
# Задание-3: вычислите площади треугольников образованных из точек одного цвета(зеленый и красный)
# для вычисления площади можно использовать формулу Герона:
# math.sqrt(p * (p-a) * (p-b) * (p-c)), где p - это полупериметр

# Групируем точки по их цвету
reds = [point for point in points if point.color == "red"]
greens = [point for point in points if point.color == "green"]

print("Площадь красного треугольника = ", calc_area(*reds))
print("Площадь зеленого треугольника = ", calc_area(*greens))
