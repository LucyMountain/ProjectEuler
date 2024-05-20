
l = [1, 1]
while True:
    n = l[-1] + l[-2]
    l.append(n)
    if len(str(n)) >= 1000:
        break

print(len(l))
