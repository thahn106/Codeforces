import heapq

for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    q = []
    ans = 0
    for c in s:
        if c:
            heapq.heappush(q, -c)
        else:
            x = 0
            if q:
                x = -heapq.heappop(q)
            ans += x
    print(ans)
