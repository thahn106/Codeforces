from math import gcd
for t in range(int(input())):
    n = int(input())
    while True:
        d = sum(list(map(int,list(str(n)))))
        if gcd(n,d)>1:
            print(n)
            break
        else:
            n+=1
