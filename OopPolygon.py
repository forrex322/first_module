import math


class Polygon:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def perimeter(self):
        raise NotImplementedError("Error")

    def area(self):
        raise NotImplementedError("Error")


class Triangle(Polygon):

    def perimeter(self):
        return self.x + self.y + self.z

    def area(self):
        p = (self.x + self.y + self.z) / 2
        return math.sqrt(p * (p - self.x) * (p - self.y) * (p - self.z))

    def type_of_triangle(self):
        if self.x == self.y == self.z:
            return print('Triangle is equilateral')

        if self.z ** 2 == self.x ** 2 + self.y ** 2:
            return print('Triangle is rectangular')
        return 1


class Rectangle(Polygon):

    def perimeter(self):
        return (self.x + self.y) * 2

    def area(self):
        return self.x * self.y

    def whether_rectangle_is_a_square(self):
        if self.x == self.y:
            print('Given rectangle is a square')
        else:
            print('Give rectangle is not a square')


class Circle(Polygon):

    def perimeter(self):
        return 2 * 3.14 * self.x

    def area(self):
        return 3.14 * self.x ** 2


print('Triangle')
a = Triangle(3, 4, 5)
print(a.area())
print(a.perimeter())
print(a.type_of_triangle())

print('\nRectangle')
b = Rectangle(2, 4)
print(b.perimeter())
print(b.area())
print(b.whether_rectangle_is_a_square())

print('\nCircle')
c = Circle(3)
print(c.area())
print(c.perimeter())
