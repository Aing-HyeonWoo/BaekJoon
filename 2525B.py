now = list(map(int, input().split()))
time = int(input())

now[1] += time
now[0] += int(now[1] // 60)
now[1] = int(now[1] % 60)

if now[0] >= 24:
    now[0] -= 24

print(now[0], now[1])