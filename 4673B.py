
st = set(range(1, 10001))
a = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    a.add(i)

b = sorted(st - a)
for i in b:
    print(i)

