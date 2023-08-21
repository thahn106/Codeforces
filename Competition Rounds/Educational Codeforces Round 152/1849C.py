import sys
import bisect

input = sys.stdin.readline

for t in range(int(input())):
    n,m = map(int, input().split())
    s = input().strip()
    
    search = []
    ref = []
    last = None
    for i,c in enumerate(s):
        if c != last:
            last = c
            search.append(i)
            ref.append(c)

    null = False
    s = set()
    for i in range(m):
        l,r = map(int, input().split())
        l -= 1
        r -= 1
        L = bisect.bisect_right(search, l)
        R = bisect.bisect_right(search, r)
        if L == R:
            null = True
        if L!=R:
            if r+1 < n and ref[R] == '0':
                R = bisect.bisect_left(search, r+1)
            if l>0 and ref[L] == '1':
                L = bisect.bisect_right(search, l-1)
            s.add((L,R))

        
    if null:
        s.add((0,0))
    print(f"{len(s)=}")





            




