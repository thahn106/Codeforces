for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    found = False
    red = 0
    blue = a[0]
    for x in range(1, (n+1)//2):
        red += a[-x]
        blue += a[x]
        if red>blue:
            found = True
            break
    if found: print("YES")
    else: print("NO")
