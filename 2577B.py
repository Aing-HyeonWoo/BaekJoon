num = 1

num *= int(input())
num *= int(input())
num *= int(input())

s = str(num)
for i in range(0, 10):
    print(s.count(str(i)))
