for t in range(int(input())):
    n = int(input())
    ans = (n * (n + 1)) // 2
    i = 1
    while i <= n:
        i *= 2
        ans -= i
    print(ans)
