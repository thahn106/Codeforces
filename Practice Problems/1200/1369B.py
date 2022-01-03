for t in range(int(input())):
    n = int(input())
    s = input()
    start =0
    working = True
    while working and start < n:
        if s[start]=='0':
            start+=1
        else:
            working = False
    end = n-1
    working = True
    while working and end >= 0:
        if s[end]=='1':
            end-=1
        else:
            working = False
    if start>end or start>=n or end < 0:
        print(s)
    else:
        ans = s[:start] + "0" +  s[(end+1):]
        print(ans)
