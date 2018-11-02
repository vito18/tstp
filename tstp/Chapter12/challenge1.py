class Apple:
    def __init__(self, w, c, p, s):
        self.weight = w
        self.color = c
        self.place = p
        self.sugar = s
        print("Created")

ap1 = Apple(5, "red", "Aomori", "10")
print(ap1.weight)
print(ap1.color)
print(ap1.place)
print(ap1.sugar)
