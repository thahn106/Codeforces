import sys

input = sys.stdin.readline

for t in range(int(input())):
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    for i,p in enumerate(P):
        if i+1 == p:
            count += 1
    r,d = divmod(count,2)
    print(r+d)