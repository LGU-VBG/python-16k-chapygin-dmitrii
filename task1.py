from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = 2 * value
        self._area = pi * value**2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return self._area

circle = Circle(5)
print(circle.radius)
print(circle.diameter)
print(round(circle.area))
