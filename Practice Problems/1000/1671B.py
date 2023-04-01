for t in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    if x[-1] - x[0] - n + 1 <= 2:
        print("YES")
    else:
        print("NO")
