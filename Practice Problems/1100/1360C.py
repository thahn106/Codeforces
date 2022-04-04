for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    possible = not (sum(a)%2)
    for i in range(1,n):
        if a[i]-a[i-1]==1:
            possible = True
            break
    if possible:
        print("YES")
    else:
        print("NO")
