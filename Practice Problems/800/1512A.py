for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    if s[0]!=s[1]:
        if s[0]==s[2]:
            ans = 2
        else:
            ans = 1
    else:
        main = s[0]
        for i in range(2,n):
            if s[i] != main:
                ans = i+1
    print(ans)
