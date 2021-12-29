for t in range(int(input())):
    n = int(input())
    ans = [i for i in range(n)]
    ans[0] = n
    print(*ans)
