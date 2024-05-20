with open("problem_13_input", "r") as inp:
    numbers = [int(line) for line in inp.readlines()]

total = sum(numbers)
print(str(total)[:10])
