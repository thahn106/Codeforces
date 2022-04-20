for t in range(int(input())):
    n, k = map(int, input().split())
    q, r = divmod(n, 3)
    print('abc'*q+'abc'[:r])
