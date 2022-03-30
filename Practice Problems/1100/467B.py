n,m,k = map(int,input().split())
other = [int(input()) for i in range(m)]
F = int(input())
ans = 0
for i in other:
    if sum(list(map(int,list(bin(i^F)[2:]))))<=k:
        ans+=1
print(ans)
