
l = []

for a in range(2, 101):
    for b in range(2, 101):
        l.append(a ** b)

l = list(dict.fromkeys(l))
print(len(l))
