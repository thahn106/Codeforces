import math
x = int(input())
ans = (1,x)
for i in range(1,math.ceil(math.sqrt(x))+1):
    if x%i==0 and math.gcd(x//i, i)==1:
        ans = (i, x//i)
print(*ans)
