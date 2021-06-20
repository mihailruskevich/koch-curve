from math import sqrt

import matplotlib.pyplot as plt

from koch_curve import Line, Point
from utils import convert_lines

a, d = 100, 10
h = a * sqrt(3) / 2
order = 4

lines = [
    Line(Point(d, h + d), Point(a + d, h + d)),
    Line(Point(a / 2 + d, d), Point(d, h + d)),
    Line(Point(a + d, h + d), Point(a / 2 + d, d)),
]

xy_points_list = map(lambda line: convert_lines(line.koch_curve(order)), lines)
for xy_points in xy_points_list:
    plt.plot(*xy_points, c='g')

plt.axis('scaled')
plt.title(f'Koch Snowflake ({order=})')
plt.savefig('res/koch-snowflake.png')
plt.show()
