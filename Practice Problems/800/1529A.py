for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = n
    for i in a:
        if i == min(a): ans -=1
    print(ans)
