
"""
class ClassName(parent1, parent2 .... parentN):
    body of class
"""


class Point:
    class_name = 'Point'

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_point(self):
        print(self.__class__.class_name)
        print('x =', self.x)
        print('y =', self.y)

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)


pt1 = Point()
print(type(pt1))
print(pt1.x)
pt1.x = 25
pt1.print_point()

pt2 = Point(34, 67)
print(pt2.x)
pt2.print_point()

print(Point.class_name)
Point.class_name = 'Test name'
pt1.print_point()
pt2.print_point()

pt3 = pt1 + pt2
pt3.print_point()
