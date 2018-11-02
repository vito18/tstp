class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h
        print("Created")

    def area(self):
        return self.base * self.height / 2

tri1 = Triangle(10, 20)
print(tri1.base)
print(tri1.height)
print(tri1.area())
