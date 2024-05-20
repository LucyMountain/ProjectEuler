import itertools

l = [str(i) for i in range(10)]
perms = list(itertools.permutations(l))
perms.sort()
print(int(''.join(perms[int(1e6) - 1])))
