import matplotlib.pyplot as plt

from koch_curve import Line, Point
from utils import convert_lines

order = 4
koch_lines = Line(Point(20, 10), Point(300, 10)).koch_curve(order)
xy_points = convert_lines(koch_lines)

plt.plot(*xy_points, c='g')
plt.axis('scaled')
plt.title(f'Koch ({order=})')
plt.savefig('res/koch.png')
plt.show()
