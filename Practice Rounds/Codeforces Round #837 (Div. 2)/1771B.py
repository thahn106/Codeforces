for t in range(int(input())):
    n, m = map(int, input().split())
    last = [n]*n
    for i in range(m):
        a,b = map(int, input().split())
        a,b = min(a,b), max(a,b)
        last[a-1] = min(last[a-1],b-1)
    ans = 0
    k = n-1
    for i in range(n):
        cur = n-1-i
        k = min(k,last[cur]-1)
        ans += (k-cur+1)
    print(ans)