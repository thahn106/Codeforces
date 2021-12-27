n = int(input())
ans = [2 for i in range(n//2)]
if n%2:
    ans[0]=3
print(len(ans))
print(*ans)
