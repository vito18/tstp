class Shape():
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a Shape")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return self.width * 2 + self.len *2

class Square(Shape):
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4

rec1 = Rectangle(20, 10)
rec1.what_am_i()
sq1 = Square(20)
sq1.what_am_i()
