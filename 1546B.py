count = int(input())
score = list(map(int, input().split()))
fix = []

score = sorted(score)
m = score[-1]

for sc in score:
    fix.append(sc / m * 100)

print(sum(fix) / count)