for t in range(int(input())):
    a,b = map(int,input().split())
    s = list(input())
    n = a+b
    q = 0
    possible = True
    if a%2 and b%2:
        possible = False
    else:
        for i in range((n+1)//2):
            j = n-1-i
            if i ==  ((n+1)//2)-1  and n%2:
                if s[i]=='?':
                    q+=1
            else:
                if s[i]=='?' and s[j] == '?':
                    q+=2
                elif s[i]=='?':
                    s[i]=s[j]
                elif s[j]=='?':
                    s[j]=s[i]
                elif s[i]!=s[j]:
                    possible = False
        for c in s:
            if c == '0':
                a -= 1
            elif c == '1':
                b -= 1
        for i in range((n+1)//2):
            j = n-1-i
            if i ==  ((n+1)//2)-1  and n%2:
                if s[i]=='?':
                    if a>0:
                        s[i]='0'
                        a -= 1
                    elif b>0:
                        s[i]='1'
                        b -= 1
            else:
                if s[i]=='?':
                    if a>=2:
                        s[i]='0'
                        s[j]='0'
                        a -=2
                    elif b>=2:
                        s[i]='1'
                        s[j]='1'
                        b-=2
    if a!=0 or b!=0:
        possible = False
    if not possible:
        print(-1)
    else:
        print("".join(s))
