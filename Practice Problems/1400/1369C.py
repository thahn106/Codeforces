for t in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    w = list(map(int,input().split()))
    a.sort(reverse = True)
    w.sort()
    ans = 0
    ind = k
    for i in range(k):
        d = w[i]-1
        temp = [a[i]]+a[ind:ind+d]
        ind += d
        ans += max(temp) + min(temp)
    print(ans)
