from math import gcd

for q in range(int(input())):
    s = input()
    t = input()
    g = gcd(len(s), len(t))
    s,t = s*(len(t)//g), t*(len(s)//g)
    if s == t:
        print(s)
    else:
        print("-1")
