for t in range(int(input())):
    n = int(input())
    s = list(input())
    p = sorted(s)
    ans = 0
    for a,b in zip(s,p):
        if a!=b:
            ans +=1
    print(ans)
