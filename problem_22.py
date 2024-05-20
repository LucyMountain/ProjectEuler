import string


def name_score(name, pos, alphabet):
    score = 0
    for char in name:
        score += alphabet.index(char) + 1
    return score * pos


with open("problem_22_input", "r") as inp:
    names = [line for line in inp.readlines()[0][1:-1].split('","')]


alphabet_upper = list(string.ascii_uppercase)
scores = []
names.sort()
print(name_score('COLIN', names.index('COLIN') + 1, alphabet_upper))
for i in range(len(names)):
    s = name_score(names[i], i + 1, alphabet_upper)
    scores.append(s)

print(sum(scores))
