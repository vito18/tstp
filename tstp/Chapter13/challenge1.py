class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return self.width * 2 + self.len *2

class Square():
    def __init__(self, l):
        self.len = l

    def calculate_perimeter(self):
        return self.len * 4

rec1 = Rectangle(20, 10)
sq1 = Square(20)
print(rec1.calculate_perimeter())
print(sq1.calculate_perimeter())
