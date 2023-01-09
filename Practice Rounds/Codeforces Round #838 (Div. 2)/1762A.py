for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    ans = 100
    for i in a:
        s += i
        sign = i%2
        cur = 0
        while i%2 == sign:
            cur +=1
            i = i//2
        ans = min(ans,cur)
    if s%2:
        print(ans)
    else:
        print(0)