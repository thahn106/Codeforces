for _ in range(int(input())):
    input()
    ref = "meow"
    ans = [0, 0, 0, 0]
    cur = 0
    pos = True
    for c in input():
        C = c.lower()
        if C == ref[cur]:
            ans[cur] += 1
        else:
            if cur < 3 and C == ref[cur + 1]:
                cur += 1
                ans[cur] += 1
            else:
                pos = False
                break
    if pos and min(ans) > 0:
        print("YES")
    else:
        print("NO")
