for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    prevc = 0
    prevv = -1
    cur = -1
    last = -1
    ans = 0
    for x in a:
        if x == last:
            cur += 1
            if prevc < cur:
                ans += 1
        elif x == last + 1:
            prevv = last
            prevc = cur
            cur = 1
        else:
            prevc = 0
            prev = 0
            cur = 1
            ans += 1
        last = x
    print(ans)
