class Person():
    def __init__(self):
        self.name = "Bob"

def true_or_false(x, y):
    return x is y

bob = Person()
same_bob = bob
another_bob = Person()

print(true_or_false(bob, same_bob))
print(true_or_false(bob, another_bob))
