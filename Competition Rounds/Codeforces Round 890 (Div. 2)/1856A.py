import sys

input = sys.stdin.readline

for t in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1,N):
        if a[i]<a[i-1]:
            ans = max(ans, a[i-1])
    print(ans)