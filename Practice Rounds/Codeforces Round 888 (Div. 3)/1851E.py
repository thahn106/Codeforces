import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

for t in range(int(input())):
    n, k = map(int, input().split())
    costs = [None] * n
    p = list(map(int, input().split()))
    for x in p:
        costs[x - 1] = 0

    print(sum(costs))
