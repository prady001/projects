from classes import Point

p1 = Point(4, 1)
p2 = Point(7, 5)
d = p1.distance_to(p2)
print(f'A distância de ({p1.x}, {p1.y}) a ({p2.x}, {p2.y}) é {d:.2f}')
