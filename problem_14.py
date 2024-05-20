

def find_collatz_sequence(num):
    terms = 1
    while num != 1:
        if num % 2 == 0:
            num = int(num // 2)
        else:
            num = (3 * num) + 1
        terms += 1
    return terms


highest_n = 0
highest_t = 0
for n in range(1, int(1e6)):
    t = find_collatz_sequence(n)
    if t > highest_t:
        highest_t = t
        highest_n = n

print(highest_n)
