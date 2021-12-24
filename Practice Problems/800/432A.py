n,k = map(int,input().split())
ans = 0
for i in input().split():
    if int(i)<=5-k:
        ans +=1
print(ans//3)
