for t in range(int(input())):
    n, x, a, b = map(int,input().split())
    a,b = min(a,b), max(a,b)
    print(min(b-a+x, n-1))
