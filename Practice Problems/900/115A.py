n = int(input())
graph =  [[] for i in range(n)]
q = []
for i in range(n):
    j = int(input())
    if j != -1:
        graph[j-1].append(i)
    else:
        q.append(i)

vst = [False for i in range(n)]
depth = [1 for i in range(n)]
order = []
while q:
    cur_node = q.pop()
    order.append(cur_node)
    vst[cur_node] = True
    for nbr in graph[cur_node]:
        if not vst[nbr]:
            q.append(nbr)
            depth[nbr] = depth[cur_node]+1
print(max(depth))
