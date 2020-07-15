# inheritance example


class Animal:

    def __init__(self, legs, eyes):
        self.legs = legs
        self.eyes = eyes

    def eat(self):
        print("I eat to live")

    def breath(self):
        print("I need oxygen to survive")

    def locomotion(self):
        print("I need to locomote to differentiate me with vegetation")

    def __str__(self):
        return "Legs " + str(self.legs) + " Eyes " + str(self.eyes)


# inheriting most of the behaviour Animals have
class Dog(Animal):
    pass


my_dog = Dog(4, 2)

print(my_dog)
my_dog.eat()
