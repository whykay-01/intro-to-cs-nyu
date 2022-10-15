
class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        # return "(" + str(self.x) + "," + str(self.y) + ")" # (x,y)
        return "({0},{1})".format(self.x, self.y)

    def distance_from_origin(self):
        distance = (self.x**2 + self.y**2) ** 0.5
        return distance

    def midpoint(self, other):
        mx = (self.x + other.x) / 2
        my = (self.y + other.y) / 2
        return Point(mx, my)

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Rectangle:

    def __init__(self, x, y, w, h):
        self.p = Point(x, y)
        self.w = w
        self.h = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.p, self.w, self.h) # ((x,y), w, h)

    def resize(self, dw, dh):
        self.w += dw
        self.h += dh

    def move(self, dx, dy):
        self.p.x += dx
        self.p.y += dy

# p1 = Point(4, 3)
# p2 = Point(2, 6)
# print(p1)
# print(p1.distance_from_origin())

# p3 = p1.midpoint(p2)
# print(p3)
# print(p3.distance_from_origin())
# p4 = p3.midpoint(p1)
# print(p4)
# print(p4.distance_from_origin())
# print(p3.distance(p4))

p5 = Point(5,5)
r1 = Rectangle(10, 5, 10, 20)
print(r1)
p5.x = 10
print(r1)
r1.move(20,-2)
print(r1)
print(p5)
