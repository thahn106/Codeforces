import sys

input = sys.stdin.readline

for t in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))

    b = [((-x)%k, i) for i, x in enumerate(a)]
    b.sort()
    ans = [i+1 for _, i in b]
    print(*ans)

