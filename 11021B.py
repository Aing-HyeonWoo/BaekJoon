import sys

arr = []
count = 1
num = int(sys.stdin.readline())

for i in range(0, num):
    arr.append(list(map(int, sys.stdin.readline().split())))

for x, y in arr:
    print(f"Case #{count}:", x + y)
    count += 1