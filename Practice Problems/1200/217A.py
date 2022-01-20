import sys
input = sys.stdin.buffer.readline

N = int(input())

pts = []
for i in range(N):
    a,b = map(int,input().split())
    pts.append((a,b))

graph = [[] for i in range(N)]

for i in range(N):
    x,y = pts[i]
    for j in range(i+1,N):
        a,b = pts[j]
        if x==a or y==b:
            graph[i].append(j)
            graph[j].append(i)



vst = [False for i in range(N)]
cc = 0
for i in range(N):
    if not vst[i]:
        q = [i]
        cc +=1
        while q:
            cur_node = q.pop()
            if not vst[cur_node]:
                vst[cur_node] = True
                for nbr in graph[cur_node]:
                    if not vst[nbr]:
                        q.append(nbr)

print(cc-1)
