

def is_prime(num, l):
    for i in l:
        if num % i == 0:
            return False
    return True


def find_primes(num):
    prime_numbers = [2]
    for i in range(3, num ** 2):
        if is_prime(i, prime_numbers):
            prime_numbers.append(i)
            if len(prime_numbers) == num:
                return prime_numbers
    return prime_numbers


primes = find_primes(10001)
print(primes[-1])