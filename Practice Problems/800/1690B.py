for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dif = 10**18
    ans = "YES"
    for x, y in zip(a, b):
        if y:
            dif = min(x - y, dif)
    for x, y in zip(a, b):
        if x - y > dif:
            ans = "NO"
            break
        if y and (x - y) < dif:
            ans = "NO"
            break
    if dif < 0:
        ans = "NO"
    if dif == 10**18:
        ans = "YES"
    print(ans)
