for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    start = False
    gap = 0
    ans = 0
    for i in a:
        if i:
            if gap:
                ans+=gap
                gap=0
            start = True
        elif start:
            gap +=1
    print(ans)
