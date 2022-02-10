from math import sqrt, floor
n,k = map(int,input().split())
a2 = 2*(k+n)
if a2 ==4:
    a = 1
elif a2 ==7:
    a = 2
else:
    a = floor(sqrt(a2))-1
print(n-a)
