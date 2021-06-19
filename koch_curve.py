from math import cos, sin, pi

ROTATION_ANGLE = pi / 3
RATIO = 1 / 3


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str((self.x, self.y))

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, ratio: float):
        return Point(self.x * ratio, self.y * ratio)

    def _rotate_x(self, angle: float):
        return self.x * cos(angle) - self.y * sin(angle)

    def _rotate_y(self, angle: float):
        return self.x * sin(angle) + self.y * cos(angle)

    def _rotate(self, angle: float):
        return Point(self._rotate_x(angle), self._rotate_y(angle))

    def scale(self, scale_from: 'Point', ratio: float):
        return (self - scale_from) * ratio + scale_from

    def rotate(self, rotation_point: 'Point', angle: float):
        return (self - rotation_point)._rotate(angle) + rotation_point


class Line:

    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b

    def bend_point(self, ratio: float):
        return self.point_b.scale(self.point_a, ratio)

    def rotation_point(self):
        return self.bend_point(RATIO)

    def point_to_rotate(self):
        return self.bend_point(2 * RATIO)

    def angle_point(self):
        return self.point_to_rotate().rotate(self.rotation_point(), ROTATION_ANGLE)

    def transform_line(self) -> list['Line']:
        return [
            Line(self.point_a, self.rotation_point()),
            Line(self.rotation_point(), self.angle_point()),
            Line(self.angle_point(), self.point_to_rotate()),
            Line(self.point_to_rotate(), self.point_b)
        ]

    def create_lines(self, lines: list['Line'], order: int) -> list['Line']:
        return lines if order <= 0 else self.create_lines(
            [v for line in lines for v in line.transform_line()],
            order - 1
        )

    def koch_curve(self, order: int) -> list['Line']:
        return self.create_lines([self], order)
