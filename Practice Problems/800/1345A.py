for t in range(int(input())):
    n,m = map(int,input().split())
    if min(n,m) == 1 or max(n,m)<=2:
        print("YES")
    else:
        print("NO")
