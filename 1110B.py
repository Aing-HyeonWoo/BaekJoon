n = int(input())
a = n
str1 = ''
str2 = ''
hap = 0
count = 0

while True:
    count += 1
    if n < 10:
        n = '0'+str(n)

    str1 = str(n)[0]
    str2 = str(n)[1]
    hap = int(str1) + int(str2)
    n = int(str2 + str(hap)[-1])
    if n == a:
        break
print(count)
