class Figure:
    sides_count = 0

    def __init__(self, __color, *new_sides):
        self.__color = __color
        self.filled = True

        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else:
            self.__sides = [1] * self.sides_count  # Default sides

    def get_color(self):
        return self.__color

    def _is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def _is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        if self._is_valid_sides(*self.__sides):
            return sum(self.__sides)
        return None

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, radius, *new_sides):
        super().__init__(__color, *new_sides)
        self.radius = radius
        self.__sides = [1]

    def get_square(self):
        return 3.14 * self.radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *new_sides):
        super().__init__(__color, *new_sides)

    def get_square(self):
        half_perimeter = sum(self.__sides) / 2
        return (half_perimeter *
                (half_perimeter - self.__sides[0]) *
                (half_perimeter - self.__sides[1]) *
                (half_perimeter - self.__sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, side_length, *new_sides):
        super().__init__(__color, *new_sides)
        self.__sides = [side_length] * self.sides_count  # 12 sides of equal length

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
