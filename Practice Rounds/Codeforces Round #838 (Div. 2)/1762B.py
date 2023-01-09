from math import log, ceil
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i,c in enumerate(a):
        m = 2 **(ceil(log(c,2)))
        if m>c:
            ans.append((i+1,m-c))
    print(len(ans))
    for a,b in ans:
        print(a,b)
