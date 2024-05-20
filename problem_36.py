

def is_palindrome(num):
    if int(str(num)[::-1]) == num:
        num_bin = int(bin(num).replace("0b", ""), 2)
        if int(str(num_bin)[::-1]) == num_bin:
            return True
    return False


l=[]
for n in range(int(1e6)):
    if is_palindrome(n):
        l.append(n)

print(sum(l))
