N,M = map(int,input().split())
c = [0]*M
r = []
for i in range(N):
    s = input()
    if 'S' in s:
        r.append(1)
    else:
        r.append(0)
    for m in range(M):
        if s[m]=='S':
            c[m]=1

print(N*M-sum(r)*sum(c))
