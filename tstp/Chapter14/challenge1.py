class Square():
    square_list = []

    def __init__(self, radius):
        self.radius = radius
        self.square_list.append(self.radius)

sq1 = Square(10)
sq2 = Square(20)
sq3 = Square(100)

print(Square.square_list)
