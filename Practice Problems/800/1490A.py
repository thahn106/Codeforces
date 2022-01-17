for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(1,n):
        b,c = min(a[i-1:i+1]),max(a[i-1:i+1])
        while 2*b<c:
            b*=2
            ans +=1
    print(ans)
