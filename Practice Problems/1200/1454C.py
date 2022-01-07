for t in range(int(input())):
    n=int(input())
    a = list(map(int,input().split()))
    cur = 0
    nd = []
    for i in a:
        if i!=cur:
            nd.append(i)
            cur = i
    counts = {}
    for i in range(len(nd)):
        a = nd[i]
        if a not in counts:
            counts[a]=1
        if not (i==0 or i==len(nd)-1):
            counts[a]+=1
    ans = n
    for a in counts:
        ans = min(ans,counts[a])
    if len(nd)==1:
        ans = 0
    print(ans)
