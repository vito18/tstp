class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

rid1 = Rider("Nocchi")
print(rid1.name)
uma = Horse("Perfume", rid1)
print("{} ride on {}".format(uma.rider.name, uma.name))
