import abc


class Shape(abc.ABC):

    @abc.abstractmethod
    def get_area(self) -> float:
        pass


class Circle(Shape):
    PI: float = 3.14159

    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self) -> float:
        return self.PI * pow(self.radius, 2)


class Rectangle(Shape):

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def get_area(self) -> float:
        return self.width * self.length


class Triangle(Shape):

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def get_area(self) -> float:
        return 0.5 * (self.base * self.height)
