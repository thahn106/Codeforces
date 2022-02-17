n = int(input())
a = list(map(int,input().split()))
neg = 0
ans = 0
zeroes = 0
for i in a:
    if i<0:
        neg+=1
        ans += (-1-i)
    elif i>0:
        ans += (i-1)
    else:
        zeroes+=1
        ans+=1
if (not zeroes) and neg%2:
    ans +=2
print(ans)
