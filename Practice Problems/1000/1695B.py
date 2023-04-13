for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2:
        print("Mike")
    else:
        mi = 2 * 10**9
        ans = "Mike"
        for i, c in enumerate(a):
            if c < mi:
                mi = c
                if i % 2:
                    ans = "Mike"
                else:
                    ans = "Joe"
        print(ans)
