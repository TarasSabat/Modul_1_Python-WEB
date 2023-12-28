from math import pi


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

class Square:
    def __init__(self, side: float):
        self.side = side


class AreaCalculator:
    def __init__(self, shapes: list[Rect]):
        self.shapes = shapes

    def total_area(self) -> float:
        sum = 0
        for el in self.shapes:
            if isinstance(el, Rect):
                sum += el.width * el.height
            if isinstance(el, Circle):
                sum += el.radius**2 * pi
            if isinstance(el, Square):
                sum += el.side**2
        return sum


if __name__ == '__main__':

    ar_sh = AreaCalculator([Rect(10, 10), Rect(4, 5), Circle(20), Rect(3, 3)])
    area = ar_sh.total_area()
    print(area)

    # Согласно принципу Open-closed перенести расчет площади в классы Rect и Circle