__author__ = 'Michael Womack'

import math

def eval(x, poly):
    sum = 0

    for i in poly:
        sum += i * math.pow(x, poly.index(i))

    return sum


def bisection(a, b, poly, tolerance):

    if eval(a, poly) * eval(b, poly) > 0:
        raise ValueError("Poly(a) and Poly(b) must have opposite signs!")

    while abs(a - b) > tolerance:
        mid = (a + b) / 2.0
        val = eval(mid, poly)
        if val == 0:
            return mid
        elif val < 0:
            a = mid
        else:
            b = mid

    return mid

