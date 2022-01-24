for t in range(int(input())):
    n = int(input())
    ans = [2*(1+i//2)-i%2 for i in range(n)]
    if n%2:
        ans[-3]=n
        ans[-2]=n-2
        ans[-1]=n-1
    print(*ans)
