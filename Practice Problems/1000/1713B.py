for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    f1, f2 = 0, 0
    pos = True
    for i in range(1, n):
        if a[i] > a[i - 1]:
            if f1:
                pos = False
        elif a[i] < a[i - 1]:
            f1 = 1
    if pos:
        print("YES")
    else:
        print("NO")
