import heapq

for t in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    heapq.heapify(a)
    for j in b:
        heapq.heappop(a)
        heapq.heappush(a, j)
    print(sum(a))
