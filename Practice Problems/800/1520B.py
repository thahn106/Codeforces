for t in range(int(input())):
    n = input()
    ans = (len(n)-1)*9
    m = n[0]*len(n)
    ans+=int(n[0])-1
    if int(n)>=int(m):
        ans+=1
    print(ans)
