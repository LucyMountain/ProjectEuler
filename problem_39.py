"""
a**2 + b**2 = c**2
if a is odd, b = (a**2 - 1) / 2, c = (a**2 + 1) / 2
if a is even, b = (a**2 / 4) - 1, c = (a**2 / 4) + 1
"""
import numpy


def find_triples(total):
    for a in range(3, total):
        if a % 2 == 0:
            b = (a**2 / 4) - 1
            c = (a**2 / 4) + 1
        else:
            b = (a**2 - 1) / 2
            c = (a**2 + 1) / 2
        if a + b + c == total:
            return [a, b, c]
        t = 0
        n = 2
        while t <= total:
            a1 = a * n
            b1 = b * n
            c1 = c * n
            n += 1
            t = a1 + b1 + c1
            if t == total:
                return [a1, b1, c1]


triple = find_triple(1000)
print(numpy.prod(triple))
