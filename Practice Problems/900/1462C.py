for t in range(int(input())):
    x = int(input())
    if x>45:
        print(-1)
    else:
        m = 9
        ans = ""
        while x:
            d = min(x, m)
            x -= d
            ans = str(d)+ans
            m -= 1
        print(ans)
