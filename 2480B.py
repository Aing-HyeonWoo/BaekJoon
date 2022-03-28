arr = list(map(int, input().split()))
count = 0
high = 0
for i in arr:
    if arr.count(i) > count:
        count = arr.count(i)
        b_key = i
    if i > high:
        high = i

if count == 3:
    print(10000 + (b_key * 1000))
elif count == 2:
    print(1000 + (b_key * 100))
else:
    print(high * 100)





