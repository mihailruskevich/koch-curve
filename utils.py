def convert_lines(lines):
    x_points, y_points = [], []
    for x in lines:
        x_points.extend([x.point_a.x, x.point_b.x])
        y_points.extend([x.point_a.y, x.point_b.y])
    return x_points, y_points
