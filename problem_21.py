

def d(num):
    factors = []
    for i in range(1, int(num // 2 + 1)):
        if num % i == 0:
            factors.append(i)
    return sum(factors)


amicable_numbers = []
lst = [i for i in range(1, 10000)]
while len(lst) > 0:
    a = lst[0]
    d_a = d(a)
    while True:
        if d_a in lst:
            if d_a == a:
                lst.remove(a)
                break
            else:
                d_b = d(d_a)
                if d_b == a:
                    amicable_numbers.append(a)
                    amicable_numbers.append(d_a)
                    lst.remove(a)
                    lst.remove(d_a)
                    break
                else:
                    a = d_a
                    d_a = d_b
        else:
            lst.remove(a)
            break


print(sum(amicable_numbers))
