count = int(input())
arr = []
r_score = 0
pl = 1

for i in range(0, count):
    arr.append(list(input()))


def c(score, s, index, sc):

    if s[index] == 'O':
        score += sc # 1

        s[index] = 'X'
        if index < len(s)-1:
            c(score, s, index+1, sc + 1)

    return score


for st in arr:
    for i in range(0, len(st)):
        r_score += c(0, st, i, 1)
        print(r_score)
