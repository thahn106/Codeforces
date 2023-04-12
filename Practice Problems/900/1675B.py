for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    last = 3 * 10**9 + 1
    ans = 0
    for c in a[::-1]:
        if last == 0:
            ans = -1
            break
        while c >= last:
            ans += 1
            c //= 2
        last = c
    print(ans)
