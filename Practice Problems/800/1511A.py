for t in range(int(input())):
    n = int(input())
    r = list(map(int,input().split()))
    ans = 0
    for c in r:
        if c == 1 or c == 3:
            ans +=1
    print(ans)
