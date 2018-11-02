class Square():
    def __init__(self, s):
        self.side = s

    def change_size(self, change):
        self.side += change

sq1 = Square(10)
print(sq1.side)
sq1.change_size(20)
print(sq1.side)
