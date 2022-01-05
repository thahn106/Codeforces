for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        for j in range((-2-i)%a[i] ,n,a[i]):
            if i<j and i+j+2 == a[i]*a[j]:
                ans +=1
    print(ans)
