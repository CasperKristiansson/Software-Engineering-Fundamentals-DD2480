
def area_of_triangle(p1, p2, p3):
    """
    Calculate the area of a triangle given its vertices.
    :param tuple(float, float) p1: Coordinates of the first vertex as a tuple (x1, y1)
    :param tuple(float, float) p2: Coordinates of the second vertex as a tuple (x2, y2)
    :param tuple(float, float) p3: Coordinates of the third vertex as a tuple (x3, y3)
    :return: The area of the triangle
    :rtype: float
    """
    return abs(0.5 * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])))
