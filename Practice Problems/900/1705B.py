for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for c in a[:-1]:
        if c == 0:
            if ans:
                ans += 1
        ans += c
    print(ans)
