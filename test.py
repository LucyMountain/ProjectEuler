# Champernowne's constant - project euler problem 40
numDigits = 0
f = [1, 10, 100, 1000, 10000, 100000, 1000000]
Champernowne = []
# want the 1st, 10th, 100th, 1000th, 10000th, 100000th, and 1000000th digits of the fractional part of Champernowne's constant
for i in range(1, 250000):  # arbitrary range
    for digit in str(i):
        numDigits += 1
        if numDigits in f:
            Champernowne.append(digit)

print(Champernowne)