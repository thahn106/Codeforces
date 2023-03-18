for t in range(int(input())):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    orb = [0] * 101
    for i in a:
        orb[i] += 1

    ans = 0
    for k in orb:
        ans += min(k, c)
    print(ans)
