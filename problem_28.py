
n = 1001
t = 1
m = 1
for i in range(1, int(n // 2) + 1):
    t += (4 * m) + (20 * i)
    m += 8 * i

print(t)
