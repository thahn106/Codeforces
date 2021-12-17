import math
def is_prime(k):
    if k>1:
        ans = True
        m = math.floor(math.sqrt(k))
        for i in range(2, m+1):
            if k%i==0:
                ans = False
    else:
        ans = False
    return ans

def pow2(k):
    t = math.log(k)/math.log(2)
    return abs(round(t)-t)<0.00001

for t in range(int(input())):
    n = int(input())
    if n == 1 or n == 4 or (n>2 and pow2(n)) or (n %4 == 2 and is_prime(n//2)):
        print("FastestFinger")
    else:
        print("Ashishgup")
