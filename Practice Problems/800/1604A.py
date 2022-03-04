for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i,n in enumerate(a):
        if i+ans+1<n:
            ans = n-i-1
    print(ans)
