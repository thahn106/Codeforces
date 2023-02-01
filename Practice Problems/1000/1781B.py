for t in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(n + 1):
        if not i or a[i - 1] < i:
            if i == n or a[i] > i:
                ans += 1
    print(ans)
