
total = 0
a = 1
b = 1

while (a + b) <= 4e6:
    c = a + b
    a = b
    b = c
    if b % 2 == 0:
        total += b

print(total)
