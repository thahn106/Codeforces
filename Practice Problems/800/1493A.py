from math import ceil
for t in range(int(input())):
    n,k = list(map(int,input().split()))
    ans = list(range(ceil(k/2),k))+list(range(k+1,n+1))
    print(len(ans))
    print(*ans)
