for t in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    if m == sum(a):
        print("YES")
    else:
        print("NO")
