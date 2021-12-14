import math
for t in range(int(input())):
    n,k = map(int, input().split())
    if n>=k:
        if n % k ==0:
            print(1)
        else:
            print(2)
    else:
        print(math.ceil(k/n))
