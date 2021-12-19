import math

for t in range(int(input())):
    n = int(input())
    a = math.sqrt(n/2)
    b = math.sqrt(n/4)
    if round(a) == a or round(b) == b:
        print("YES")
    else:
        print("NO")
