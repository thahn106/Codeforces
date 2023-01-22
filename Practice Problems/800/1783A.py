for t in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    if n > 1 and a[0] == a[-1]:
        print("NO")
    else:
        print("YES")
        print(*([a[-1]]+a[0:-1]))
