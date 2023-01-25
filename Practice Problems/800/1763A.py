for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    bits = [[False for i in range(2)] for j in range(10)]

    for k in a:
        d = k
        for i in range(10):
            bits[i][d % 2] = True
            d = d // 2
    ans = 0
    for i in range(10):
        if bits[i][0] and bits[i][1]:
            ans += 2**i
    print(ans)
