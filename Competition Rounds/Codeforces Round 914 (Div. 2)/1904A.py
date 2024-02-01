import sys

input = sys.stdin.readline


for t in range(int(input())):
    a, b = map(int, input().split())
    xk, yk = map(int, input().split())
    xq, yq = map(int, input().split())
    dx = [a, a, -a, -a, b, b, -b, -b]
    dy = [b, -b, b, -b, a, -a, a, -a]

    ans = set()
    for x, y in zip(dx, dy):
        nx = xk + x
        ny = yk + y
        drx = abs(nx - xq)
        dry = abs(ny - yq)
        if drx == a and dry == b:
            ans.add((nx, ny))
        elif drx == b and dry == a:
            ans.add((nx, ny))
    print(len(ans))
