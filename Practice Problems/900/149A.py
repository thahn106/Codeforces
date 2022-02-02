k = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
ans = 0
while k>0 and ans<12:
    k -= a[ans]
    ans +=1
if ans ==12 and k>0:
    ans = -1
print(ans)
