import math


def are_close_enough(a, b, tolerance=1e-4):
    return math.fabs(a - b) / a < tolerance