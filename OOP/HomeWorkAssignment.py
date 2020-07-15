# this is a homework assignment
import math


class HomeWorkAssignment:

    def __init__(self, cordinate1, cordinate2):
        self.cordinate1 = cordinate1
        self.cordinate2 = cordinate2

    def slope(self):
        x1, y1 = self.cordinate1
        x2, y2 = self.cordinate2
        return (y2 - y1) / (x2 - x1)

    def distance(self):
        x1, y1 = self.cordinate1
        x2, y2 = self.cordinate2
        dist_x = x2 - x1
        dist_y = y2 - y1
        dist_square = pow(dist_x, 2) + pow(dist_y, 2)
        return math.sqrt(dist_square)


homework_assignment = HomeWorkAssignment((3, 2), (8, 10))

print("Slope of the line : ", homework_assignment.slope())

print("Distance between the line : ", homework_assignment.distance())
