import math

factorials = [math.factorial(j) for j in range(1, 10)]

nums = []
for i in range(10, int(2.5e7)):
    s = sum([factorials[int(c) - 1] for c in str(i)])
    if s == i:
        nums.append(i)

print(i)
