import sys
def get_ints(): return list(map(int, sys.stdin.readline().split()))

from math import gcd

n = int(input())
a = get_ints()

g = gcd(a[0],a[1])
ans = a[0]*a[1]//g

for i in range(2,n):
    ans = gcd(ans, a[i]*g//gcd(g,a[i]))
    g = gcd(g,a[i])
print(ans)
