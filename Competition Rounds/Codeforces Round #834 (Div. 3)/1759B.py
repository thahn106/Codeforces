from math import sqrt, floor

def tri(N):
    n = floor(sqrt(2*N))
    return 2*N == n*(n+1)
        
for t in range(int(input())):
    m,s = map(int, input().split())
    b = sorted(list(map(int, input().split())))
    i = 0
    n = 1
    ans = "YES"
    while s>0 or i<m:
        if i<m:
            if b[i] == n:
                i+=1            
            elif b[i]>n:
                s -= n
            else:
                ans = "NO"
                break
        else:
            s -= n
        if s < 0:
            ans = "NO"
            break
        n += 1
    print(ans)

    