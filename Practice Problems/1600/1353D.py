import heapq

for t in range(int(input())):
    n = int(input())
    a = [0 for i in range(n)]
    pq = [(-n,0)]
    i = 1
    while pq:
        len,start = heapq.heappop(pq)
        len *= -1
        mid = start+((len-1)//2)
        a[mid]=i
        i+=1
        if mid>start:
            heapq.heappush(pq, (start-mid, start))
        if len+start>mid+1:
            heapq.heappush(pq, (mid+1-start-len, mid+1))
    print(*a)
