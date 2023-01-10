import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    app = {}

    q = [list(map(int, input().split())) for i in range(n)]
    for c in q:
        for k in c[1:]:
            if k in app:
                app[k] +=1
            else:
                app[k] = 1

    found = False
    for c in q:
        cur = True
        for k in c[1:]:
            if app[k] <2:
                cur = False
                break
        if cur:
            found = True
            break
    if found:
        print("Yes")
    else:
        print("No")

