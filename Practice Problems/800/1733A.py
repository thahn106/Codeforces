for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    for i in range(k):
        s += max(a[i::k])
    print(s)
