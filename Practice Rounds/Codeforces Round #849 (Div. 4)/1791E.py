for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    negs = 0
    zero = 0
    for i in range(n):
        if a[i] < 0:
            negs += 1
            a[i] *= -1
        elif a[i] == 0:
            zero += 1
    if zero or negs % 2 == 0:
        print(sum(a))
    else:
        print(sum(a) - 2 * min(a))
