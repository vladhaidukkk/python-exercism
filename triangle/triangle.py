def validate_triangle(sides):
    return (sides := sorted(sides))[0] > 0 and sum(sides[:2]) >= sides[2]


def equilateral(sides):
    return validate_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return validate_triangle(sides) and len(set(sides)) < 3


def scalene(sides):
    return validate_triangle(sides) and len(set(sides)) == 3
