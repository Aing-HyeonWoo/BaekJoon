import sys

nx = list(map(int, sys.stdin.readline().split()))

arr = list(map(int, sys.stdin.readline().split()))
array = []
str = ''
for i in arr:
    if i < nx[1]:
        array.append(i)

for j in array:
    print(j, end=' ')
