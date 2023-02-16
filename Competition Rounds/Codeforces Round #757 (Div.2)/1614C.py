import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())
    total = 0
    for line in range(m):
        l, r, x = map(int, input().split())
        total = total | x

    total = total % 1000000007
    # complexity O(n)
    for exp in range(n - 1):
        total = total * 2
        if total > 1000000007:
            total -= 1000000007
    sys.stdout.write(str(total) + "\n")
