for t in range(int(input())):
    n, k = map(int, input().split())
    left = False
    right = False
    for _ in range(n):
        a, b = map(int, input().split())
        if a == k:
            left = True
        if b == k:
            right = True
    if left and right:
        print("YES")
    else:
        print("NO")
