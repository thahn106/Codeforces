import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    k = min(a)
    if m == k:
        print("NO")
    else:
        s = ""
        maxfound = False
        minfound = False
        blue = False
        for v in a:
            if v == m and not maxfound:
                s += "R"
                maxfound = True
            elif v == k and not minfound:
                s += "R"
                minfound = True
            elif not blue:
                s += "B"
                blue = True
            else:
                s += "R"
        print("YES")
        print(s)
