import numpy

total = 0
m = 1
vals = [10 ** i for i in range(7)]
digits = []
for i in range(10):
    t = total + ((10**(m-1)) * m * 9)
    if t > vals[0]:
        n = vals[0] - total
        r = n % m
        num = (10 ** (m-1)) + int((n)//m) - 1
        d = int(str(num)[r-1])
        digits.append(d)
        vals.pop(0)
    if len(vals) < 1:
        break
    total = t
    m += 1

print(digits)
print(numpy.prod(digits))
