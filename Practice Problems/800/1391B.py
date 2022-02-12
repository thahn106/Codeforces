for t in range(int(input())):
    n,m = map(int,input().split())
    ans = 0
    for i in range(n):
        s = input()
        if i == n-1:
            for c in s:
                if c == "D":
                    ans +=1
        else:
            if s[-1]=='R':
                ans +=1
    print(ans)
