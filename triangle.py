def equilateral(sides):
    if is_valid_triangle(sides):
        return sides[0] == sides[1] == sides[2]
    return False


def isosceles(sides):
    if is_valid_triangle(sides):
        return sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]
    return False


def scalene(sides):
    if is_valid_triangle(sides):
        return not isosceles(sides)
    return False


def degenerate(sides):

    if (sides[0] + sides[1] == sides[2]) or (
            sides[1] + sides[2] == sides[0]) or (
            sides[2] + sides[0] == sides[1]):
        return True
    return False


def is_valid_triangle(sides):
    if len(sides) != 3:
        return False

    for side in sides:
        if side <= 0:
            return False

    if (sides[0] + sides[1] < sides[2]) or (
            sides[1] + sides[2] < sides[0]) or (
            sides[2] + sides[0] < sides[1]):
        if degenerate(sides):
            return True
        return False

    return True
