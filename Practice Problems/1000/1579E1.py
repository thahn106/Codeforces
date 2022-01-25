for t in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))
    ans = [-1 for i in range(n)]
    head = 0
    tail = 0
    for i in p:
        if i < ans[head]:
            head = (head-1)%n
            ans[head]=i
        else:
            ans[tail]=i
            tail = (tail+1)%n
    na = []
    for i in range(n):
        ind = (head+i)%n
        na.append(ans[ind])
    print(*na)
