for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    last = -1
    prev = None
    ans = [0] * n
    cur_size = None
    pos = True
    for i, c in enumerate(s):
        if c == cur_size:
            ans[prev] = i + 1
            prev = i
        else:
            if prev is not None:
                if prev == last:
                    pos = False
                    break
                else:
                    ans[prev] = last + 1
            last = i
            prev = i
            cur_size = c
    else:
        if prev == last:
            pos = False
        else:
            ans[prev] = last + 1
    if pos:
        print(*ans)
    else:
        print(-1)
