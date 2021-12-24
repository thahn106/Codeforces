for t in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort()
    if k<n:
        ans = a[:(n-k)]
        rest = a[(n-k):]+b
        rest.sort(reverse=True)
        ans += rest [:k]
    else:
        rest = a+b
        rest.sort(reverse=True)
        ans = rest[:n]
    print(sum(ans))
