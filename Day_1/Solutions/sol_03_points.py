class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point) -> float:
    """ Расстояние между двумя точками """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
    
    
# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
# Variant 1
zero = Point(0, 0)
max_dist = 0
max_point = points[0]
for point in points:
    curr_dist = distance(zero, point)
    if curr_dist > max_dist:
        max_dist = curr_dist
        max_point = point
print(f"Координаты наиболее удаленной точки = {max_point.x, max_point.y}")

# Variant 2
zero = Point(0, 0)
distances = []
for point in points:
    distances.append(distance(zero, point))
max_dist = max(distances)
idx_point = distances.index(max_dist)
print(f"Координаты наиболее удаленной точки = {points[idx_point].x, points[idx_point].y}")
