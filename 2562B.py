num = 0
index = -1
put = 0

for i in range(1, 10):
    put = int(input())
    if put > num:
        num = put
        index = i
print(num)
print(index)