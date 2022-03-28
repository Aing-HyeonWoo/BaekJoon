year = int(input())

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    a = 1
else:
    a = 0

print(a)

