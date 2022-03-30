min, max = map(int, input().split())

count = max - min +1

for i in range(min, max+1):
    for j in range(2, max):
        if i % (j**j) == 0:
            count -= 1
            continue
print(count)
