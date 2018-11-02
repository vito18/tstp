class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name

mick = Person("mick jagger")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner)
print(stan.owner.name)
