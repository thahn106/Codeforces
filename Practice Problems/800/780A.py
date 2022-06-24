n = int(input())
socks = [0]*n
x = list(map(int, input().split()))
ans = 0
cur = 0
for i in x:
    if socks[i-1]:
        cur -= 1
        socks[i-1] = 0
    else:
        socks[i-1] = 1
        cur += 1
        ans = max(ans, cur)
print(ans)
