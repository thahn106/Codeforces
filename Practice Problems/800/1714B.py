for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    ans = 0
    for i in range(n):
        if a[n - 1 - i] in s:
            break
        else:
            ans += 1
            s.add(a[n - 1 - i])
    print(n - ans)
