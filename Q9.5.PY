class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        print("x =", self.x, "y =", self.y)

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

p1 = Point(x1, y1)
p2 = Point(x2, y2)

p3 = p1 + p2

print("Result Point:")
p3.display()