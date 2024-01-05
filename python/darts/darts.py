import math


def score(x, y):
    radius = get_distance_from_center(x, y)
    points = 0

    if radius > 10:
        points = 0
    elif radius > 5 and radius <= 10:
        points = 1
    elif radius > 1 and radius <= 5:
        points = 5
    elif radius <= 1:
        points = 10

    return points


def get_distance_from_center(x, y):
    """
    Calculate distance from the center of a dart board (0, 0)
    """
    return math.sqrt(pow(x, 2) + pow(y, 2))
