
num = 100
sum_of_squares = sum([i ** 2 for i in range(1, num + 1)])
square_of_sum = sum([i for i in range(1, num + 1)]) ** 2

print(square_of_sum - sum_of_squares)
