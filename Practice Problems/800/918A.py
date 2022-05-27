n = int(input())
cur, next = 1, 1
ans = ""
for i in range(n):
    if i + 1 == cur:
        ans += 'O'
        cur, next = cur+next, cur
    else:
        ans += 'o'
print(ans)
