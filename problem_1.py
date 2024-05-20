

def check_multiple(num):
    if (num % 3 == 0) or (num % 5 == 0):
        return True
    else:
        return False


total = 0

for n in range(1000):
    if check_multiple(n):
        total += n

print(total)
