for T in range(int(input())):
    n,k = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    ans = 0
    for i in a[1:]:
        ans += (k-i)//a[0]
    print(ans)
