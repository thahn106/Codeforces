for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = max(a)-min(a)
    m = max(a)
    for i in range(n):
        c = a[i]
        a[i] = m-c
        if k % 2 == 0:
            a[i] = d-a[i]
    print(*a)
