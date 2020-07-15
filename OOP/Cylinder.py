# cylinder class example
import math


class Cylinder:

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * pow(self.radius, 2) * self.height

    def surface(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * pow(self.radius, 2))


cylinder_obj = Cylinder(2, 3)

print(cylinder_obj.volume())

print(cylinder_obj.surface())
