for t in range(int(input())):
    n, k = map(int, input().split())
    r = 1 + k + k * k + k * k * k
    N = n // r
    print(N, N * k, N * k * k, N * k * k * k)
