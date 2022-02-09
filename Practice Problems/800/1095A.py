n = int(input())
t = input()
i = 1
k = 1
ans = ""
while i<=n:
    ans += t[i-1]
    k+=1
    i+=k
print(ans)
