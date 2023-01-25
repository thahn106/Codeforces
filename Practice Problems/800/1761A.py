for t in range(int(input())):
    n, a, b = map(int, input().split())
    if a == b == n or n - a - b >= 2:
        print("Yes")
    else:
        print("No")
