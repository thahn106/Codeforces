from math import gcd
y,w = map(int, input().split())
n,d = 7- max(y,w), 6
g = gcd(n,d)
print("{}/{}".format(n//g,d//g))
