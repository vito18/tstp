class Hexagon():
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 6

hex1 = Hexagon(10)
print(hex1.calculate_perimeter())
