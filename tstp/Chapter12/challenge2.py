import math

class Circle:
    def __init__(self, d):
        self.diameter = d

    def area(self):
        s = math.pi * (self.diameter ** 2) / 4
        return s

cir1 = Circle(11.5)
print(cir1.diameter)
s = cir1.area()
print(s)
