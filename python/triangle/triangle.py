def equilateral(sides):
    """
    Returns True if all sides are of an equal length, False otherwise
    """
    if not validTriangle(sides):
        return False

    val = 0
    for side in sides:
        if val == 0:
            val = side
        if side != val:
            return False

    return True


def isosceles(sides):
    """
    Returns True if triangle has at least two sides the same length.
    Otherwise returns False
    """
    if not validTriangle(sides):
        return False

    sides.sort()
    if sides[0] == sides[1] or sides[2] == sides[1]:
        return True

    return False


def validTriangle(sides):
    """
    Helper function for validating triangle sides data, checks if triangle
    has at least 3 sides and if triangle equity principle is not validated.
    - Triangle equity: sum of two sides of a triangle is greater than the
    third side.
    """
    if len(sides) < 3:
        raise Exception
    if 0 in sides:
        return False
    sides.sort()
    if sides[0] + sides[1] <= sides[2]:
        return False

    return True


def scalene(sides):
    """
    Test if a triangle is scalene triangle with all sides of different
    lengths.
    """
    if not validTriangle(sides):
        return False
    sides.sort()
    for i in range(1, len(sides)):
        if sides[i] == sides[i - 1]:
            return False

    return True
