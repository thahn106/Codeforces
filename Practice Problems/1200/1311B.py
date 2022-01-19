for t in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    pos = [False for i in range(n)]
    for p in list(map(int,input().split())):
        pos[p-1] = True
    sa = a.copy()
    start = -1
    for i in range(n):
        if pos[i] and start == -1:
            start = i
        if not pos[i] and start !=-1:
            sa[start:i+1]= sorted(sa[start:i+1])
            start = -1
    if sa == sorted(sa): print("YES")
    else: print("NO")
