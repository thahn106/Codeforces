for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    ans = "YES"
    for x, y in zip(a, b):
        if (x - y) % 2:
            ans = "NO"
            break
    print(ans)
