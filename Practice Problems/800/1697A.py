for t in range(int(input())):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    print(max(0,sum(a)-m))