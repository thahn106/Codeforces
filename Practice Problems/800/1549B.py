for t in range(int(input())):
    n = int(input())
    s = list(input())
    r = input()
    ans = 0
    for i,c in enumerate(r):
        if int(c):
            if s[i]=='0':
                ans +=1
            elif i>0 and s[i-1]=='1':
                ans +=1
                s[i-1] = '2'
            elif i<n-1 and s[i+1]=='1':
                ans +=1
                s[i+1] = '2'
    print(ans)
