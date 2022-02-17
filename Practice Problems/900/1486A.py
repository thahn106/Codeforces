for t in range(int(input())):
    n = int(input())
    h = list(map(int,input().split()))
    rest = 0
    possible = True
    for i in range(n):
        h[i]+=rest
        rest = 0
        if h[i]<i:
            possible = False
            break
        else:
            rest = h[i]-i
            h[i] = i
    if possible:
        print("YES")
    else:
        print("NO")
