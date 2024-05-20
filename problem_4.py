

def is_palindrome(num):
    if num == int(str(num) [::-1]):
        return True
    else:
        return False


l = []
for i in range (100, 1000):
    for j in range(100, 1000):
        prod = i * j
        if is_palindrome(prod):
            l.append(prod)

l.sort()
print(l[-1])
