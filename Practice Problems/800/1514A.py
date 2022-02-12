from math import sqrt
def cs(n):
    return sqrt(n) == round(sqrt(n))

for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    sq = False
    for c in a:
        if not cs(c):
            sq=True
            break
    if sq:
        print("YES")
    else:
        print("NO")
