for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    d = [0]*n
    def bfs(start,end,depth):
        m =-1
        ma = 0
        for i in range(start,end+1):
            if a[i]>ma:
                ma = a[i]
                m=i
        d[m] = depth
        if start<m:
            bfs(start,m-1,depth+1)
        if m<end:
            bfs(m+1,end,depth+1)
    bfs(0,n-1,0)
    print(*d)
