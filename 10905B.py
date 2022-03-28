arr = []
count = int(input())
for i in range(0, count):
    arr.append(list(map(int, input().split())))

for x, y in arr:
    print(x + y)
