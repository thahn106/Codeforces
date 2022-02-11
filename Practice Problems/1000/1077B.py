n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(n-2):
    if a[i:i+3] == [1,0,1]:
        ans+=1
        a[i+2]=0
print(ans)
