for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ma = max(a)
    if min(a)==ma:
        print(-1)
    else:
        for i in range(n):
            if a[i]==ma:
                if (i>0 and a[i-1]<a[i]) or (i<n-1 and a[i+1]<a[i]):
                    print(i+1)
                    break
