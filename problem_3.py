

"""
def is_prime(num, l):
    for i in l:
        if num % i == 0:
            return False
    return True


def find_primes(num):
    prime_numbers = [2]
    for i in range(3, num // 2, 2):
        if is_prime(i, prime_numbers):
            prime_numbers.append(i)
    return prime_numbers


def find_primes_2(num):
    all_ints = list(range(1, num + 1))
    prime_numbers = [2]
    for i in range(3, num + 1, 2):
        if all_ints[i - 1] != 0:
            if is_prime(i, prime_numbers):
                prime_numbers.append(i)
                for j in range(i, num + 1, i):
                    all_ints[j - 1] = 0
    return prime_numbers
"""


number = 600851475143
test = 13195
prime_factors = []
primes = find_primes(number)
for p in primes:
    if number % p == 0:
        prime_factors.append(p)

print(prime_factors[-1])
