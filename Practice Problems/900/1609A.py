for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    r = 1
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] = a[i]//2
            r *= 2
    s = sum(a)
    m = max(a)
    print(s+(r-1)*m)
