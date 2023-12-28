from math import pi


class Shape:
    def area_of(self):
        raise NotImplementedError()


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area_of(self):
        return pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area_of(self):
        return self.side ** 2


class AreaCalculator:
    def __init__(self, shapes: list[Shape]):
        self.shapes = shapes

    def total_area(self) -> float:
        sum = 0
        for el in self.shapes:
            sum += el.area_of()
        return sum


if __name__ == '__main__':
    ar_sh = AreaCalculator([Rectangle(10, 10), Rectangle(4, 5), Circle(20), Rectangle(3, 3), Square(10)])
    area = ar_sh.total_area()
    print(area)
