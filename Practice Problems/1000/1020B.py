n = int(input())
p = list(map(int,input().split()))

ans = []
for i in range(n):
    visited = [False for i in range(n)]
    visited[i]=True
    cur = i
    # print("start: {}".format(cur+1))
    while True:
        cur = p[cur]-1
        # print("cur: {}".format(cur+1))
        if visited[cur]:
            ans.append(cur+1)
            break
        else:
            visited[cur]=True
print(*ans)
