n, k = map(int, input().split())
a = input().split()
ans = 0
for i in a:
    temp = 0
    for c in i:
        if c == '4' or c == '7':
            temp += 1
    if temp <= k:
        ans += 1
print(ans)
