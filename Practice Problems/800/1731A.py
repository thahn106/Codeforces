for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    for c in a:
        ans *= c
    ans += n - 1
    ans *= 2022
    print(ans)
