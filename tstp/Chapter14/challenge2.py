class Square():
    square_list = []

    def __init__(self, radius):
        self.radius = radius
        self.square_list.append(self.radius)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.radius, self.radius, self.radius, self.radius)

sq1 = Square(10)
sq2 = Square(20)
sq3 = Square(100)

print(Square.square_list)
print(sq1)
print(sq2)
print(sq3)
