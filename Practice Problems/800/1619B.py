from math import pow,floor

def rt(n,p):
    ans = floor(pow(n,1/p))
    if (ans+1)**p<=n:
        return (ans+1)
    else:
        return ans

for t in range(int(input())):
    n = int(input())
    ans = rt(n,2)+rt(n,3)-rt(n,6)
    print(ans)
