A,B = map(int,input().split())
ans = 1
for i in range(1,min(A,B)+1):
    ans *=i
print(ans)
