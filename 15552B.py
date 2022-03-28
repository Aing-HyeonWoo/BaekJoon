import sys
count = int(input())
arr = []

for i in range(0, count):
    arr.append(list(map(int, sys.stdin.readline().split())))

for x, y in arr:
    print(x + y)
