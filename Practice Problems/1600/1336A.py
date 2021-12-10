import heapq
import time
import random

class Node:
    def __init__(self, node):
        self.node = node
        self.neighbors = []
        self.prev = -1
        self.depth = 0
        self.below=0

n,k = [int(x) for x in input().split()]

starttime = time.time()
graph = []
for i in range(n):
    graph.append(Node(i))

for i in range(n-1):
    f,t = [int(x)-1 for x in input().split()]
    graph[f].neighbors.append(t)
    graph[t].neighbors.append(f)

dfs = [0]
visited = [False for i in range(n)]
visit_list = []

while dfs:
    node = dfs.pop()
    visited[node]=True
    visit_list.append(node)
    for adj in graph[node].neighbors:
        if not visited[adj]:
            dfs.append(adj)
            graph[adj].depth = graph[node].depth+1
            graph[adj].prev = node

bl = [0 for i in range(n)]
for i in range(n):
    bc=0
    node = visit_list[n-1-i]
    for adj in graph[node].neighbors:
        if adj !=graph[node].prev:
            bc += graph[adj].below+1
    graph[node].below = bc
    bl[i]=bc-graph[node].depth

bl.sort(reverse=True)
ans = 0
for i in range(n-k):
    ans += bl[i]

print(ans)
