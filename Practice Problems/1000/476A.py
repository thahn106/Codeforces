n,m = [int(x) for x in input().split()]

mod = n%m
ans = ((n//2)//m)*m+mod
if ans>n/2:
    ans -= m
if ans<0:
    ans = -1
else:
    ans = n-ans
print(ans)
