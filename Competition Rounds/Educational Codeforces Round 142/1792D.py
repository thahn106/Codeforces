class Node: 
    def __init__(self, m, depth):
        self.children = [None]*m
        self.depth = depth
        self.count = 0

    def __repr__(self):
        return str(self.children)


class Tree:
    m = 0
    def __init__(self,m):
        self.root = Node(m,0)
        self.m = m

    def add(self, perm, node):
        node.count += 1
        d = node.depth
        if d < self.m:
            if not node.children[perm[d]]:
                node.children[perm[d]] = Node(self.m, d+1)
            self.add(perm, node.children[perm[d]])

    def find(self, perm, node):
        d = node.depth
        if d+1 < self.m:
            if node.children[perm[d]-1]:
                return self.find(perm, node.children[perm[d]-1])
            return d-1
        return d


for t in range(int(input())):
    n,m = map(int, input().split())
    pt = Tree(m)
    perms = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        perm = perms[i]
        change = [0]*m
        for j in range(m):
            change[perm[j]-1] = j
        pt.add(change, pt.root)
    ans = [pt.find(perm, pt.root)+1 for perm in perms]
    print(*ans)
    
        


    