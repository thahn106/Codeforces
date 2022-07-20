for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k = len(set(a))
    if (n-k)%2:
        k -= 1
    print(k)
