
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def distance(self, other_point) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


def dict_color(in_points) -> dict:
    colors = {}  # dict[color] = [a, b, c]
    for idx in range(len(in_points) - 1):
        for j in range((idx + 1), len(in_points)):
            if in_points[idx].color == in_points[j].color:
                color = in_points[idx].color
                colors.setdefault(color, [])
                colors[color].append(in_points[j].distance(in_points[idx]))
    return colors


def area(dict_triangle: dict) -> dict:
    """ На входе словарь точек, на выходе словарь с площадями для каждого цвета"""
    areas = {}
    for key, value in dict_triangle.items():
        p = sum(value) / 2
        areas[key] = (p * (p - value[0]) * (p - value[1]) * (p - value[2])) ** 0.5
    return areas




points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]
color = dict_color(points)



print(f"Площадь красного треугольника = {area(color)["red"]:.2f}")
print(f"Площадь зеленого треугольника = {area(color)["green"]:.2f}")
