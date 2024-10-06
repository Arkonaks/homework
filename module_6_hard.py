import math

class Figure:
    sides_count = 0

    def __init__(self, sides: int, color: tuple, filled: bool):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= int(x) <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        return all(side > 0 and isinstance(side, int) for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            raise ValueError("Неправильное количество сторон.")
        self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, radius, color):
        super().__init__((2 * radius * 3.14,), color, True)
        self.__radius = radius

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, color):
        super().__init__(sides, color, True)

    def get_square(self):
        s = len(self) / 2
        a, b, c = self.get_sides()
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, edge_length, color):
        super().__init__([edge_length] * 12, color, True)

    def set_sides(self, edge_length):
        if isinstance(edge_length, int) and edge_length > 0:
            self.__sides = [edge_length] * self.sides_count

    def get_volume(self):
        edge = self.get_sides()[0]
        return edge ** 3


circle1 = Circle(10, (200, 200, 100))  # (Стороны, цвет)
cube1 = Cube(6, (222, 35, 130))

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5)  # Изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
