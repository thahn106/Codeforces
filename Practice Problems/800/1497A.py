for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = []
    for i in range(n):
        if i in a:
            ans.append(i)
            a.remove(i)
        else:
            ans = ans +a
            break
    print(*ans)
