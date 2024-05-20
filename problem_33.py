from fractions import Fraction
import numpy


def find_fracts(common, n_1, n_2):
    f = []
    com = str(common)
    num = str(n_1)
    den = str(n_2)
    nums = [int(i) for i in [com + num, num + com]]
    dens = [int(i) for i in [com + den, den + com]]
    for n in nums:
        for d in dens:
            if d > n:
                if Fraction(int(num), int(den)) == Fraction(n, d):
                    f.append([int(num), int(den)])
    return f



fracts = []
for c in range(1, 10):
    for a in range(1, 10):
        for b in range(1, 10):
            l = find_fracts(c, a, b)
            if len(l) > 0:
                for f in l:
                    fracts.append(f)

numerator = numpy.prod([i[0] for i in fracts])
denominator = numpy.prod([j[1] for j in fracts])

print(Fraction(numerator, denominator))
