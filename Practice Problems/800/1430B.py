for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(sum(a[:k+1]))
