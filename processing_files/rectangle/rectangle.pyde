import random

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

    def display(self):
        fill(255,0,0)
        rect(self.p.x, self.p.y, self.w, self.h)

    def resize(self, dw, dh):
        self.w += dw
        self.h += dh

    def move(self, x, y):
        self.p.x = x
        self.p.y = y

r1 = Rectangle(200, 200, 100, 100)

def setup():
    size(400, 400)
    background(255,255,0)
    
def draw():
    background(255,255,0)
    # ellipse(320,320, mouseX, mouseY)
    r1.move(mouseX, mouseY)
    r1.display()

def mouseClicked():
    # fill(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    r1.resize(20,20)
    print("clicked")
