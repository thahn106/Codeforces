for t in range(int(input())):
    a,s = input().split()
    ans = ""
    pos = True
    j = len(s)-1
    for i in a[::-1]:
        c = int(i)
        if j<0:
            pos = False
            break
        if int(s[j])<c:
            if j > 0 and s[j-1] == '1':
                ans = str(int(s[j-1:j+1])-c)+ans
                j -= 2
            else:
                pos = False
                break
        else:
            ans = str(int(s[j])-c)+ans
            j -= 1
    if pos:
        print(int(s[:j+1]+ans))
    else:
        print(-1)
        