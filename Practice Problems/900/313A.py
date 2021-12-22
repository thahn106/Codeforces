n = input()
ans = int(n)
for i in range(len(n)-2,len(n)):
    t = int(n[:i] + n[i+1:])
    ans = max(ans,t)
print(ans)
