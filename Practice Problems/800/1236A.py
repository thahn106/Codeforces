for t in range(int(input())):
    a,b,c = map(int,input().split())
    ans = 0
    D = min(b,c//2)
    ans += 3*D
    b -= D
    D = min(a,b//2)
    ans += 3*D
    print(ans)
