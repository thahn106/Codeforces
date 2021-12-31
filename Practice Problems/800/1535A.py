for t in range(int(input())):
    a,b,c,d = map(int,input().split())
    if min(a,b)>max(c,d) or max(a,b)<min(c,d):
        print("NO")
    else:
        print("YES")
