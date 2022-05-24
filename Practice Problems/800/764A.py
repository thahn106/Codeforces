from math import gcd
n, m, z = map(int, input().split())
print(z//(n*m//gcd(n, m)))
