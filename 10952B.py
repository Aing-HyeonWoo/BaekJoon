import sys
arr = []
temp = []

while(True):
    temp = list(map(int, sys.stdin.readline().split()))
    if temp[0] == 0 and temp[1] == 0:
        break
    else:
        arr.append(temp)

for x, y in arr:
    print(x + y)