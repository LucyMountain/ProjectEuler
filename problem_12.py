

def find_triangle_number(num_of_factors):
    n = 1
    while True:
        t_num = 0.5 * n * (n + 1)
        factors = [1, t_num]
        for i in range(2, int((t_num // 2) + 1)):
            if t_num % i == 0:
                factors.append(i)
                factors.append(t_num // i)
            factors.sort()
            if factors[-1] <= i:
                break
        if len(factors) > num_of_factors:
            return t_num
        n += 1


num_of_factors = 5
triangle_number = find_triangle_number(num_of_factors)
print(triangle_number)
