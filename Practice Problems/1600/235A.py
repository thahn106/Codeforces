from itertools import combinations
from math import gcd

def lcm(a,b):
    return (a*b)//gcd(a,b)

n = int(input())
if n<=3:
    print([1,2,6][n-1])
elif n%2:
    print(n*(n-1)*(n-2))
else:
    ans = (n-1)*(n-2)*(n-3)
    for a in combinations(range(max(1,n-50),n+1),3):
        ans = max(ans, lcm(lcm(a[0],a[1]),a[2]))
    print(ans)
