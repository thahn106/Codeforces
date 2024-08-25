import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, d = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    ref = {}
    for i, (x, y) in enumerate(points):
        ref[(x, y)] = i + 1

    def radix_0(x, y, i):
        return ((x + y) % d, (x - y) % d, x + y, x - y, x, y, i + 1)

    def radix_1(x, y, i):
        return ((x + y) % d, (x - y) % d, x - y, x + y, x, y, i + 1)

    def search(start, end, points):
        for i in range(start, end - 1):
            if (
                points[i][3] == points[i + 1][3]
                and abs(points[i][4] - points[i + 1][4]) == d
            ):
                print(ref[points[i][5:7]], ref[points[i + 1][5:7]])
                return

        return None

    point_0 = [radix_0(x, y, i) for i, (x, y) in enumerate(points)]
    point_0.sort()
    cur_rad = point_0[0][0:2]
    start = 0
    for i in range(n):
        rad = point_0[i][0:2]
        if rad != cur_rad:
            ans = search(start, i)
            start = i
        if ans is not None:
            break
    if ans is None:
        ans = search(start, n)

    point_1 = [radix_1(x, y, i) for i, (x, y) in enumerate(points)]
    point_1.sort()
    cur_rad = point_1[0][0:2]
    start = 0
    for i in range(n):
        rad = point_1[i][0:2]
        if rad != cur_rad:
            ans = search(start, i)
            start = i
        if ans is not None:
            break
    if ans is None:
        ans = search(start, n)

    if ans is None:
        print(0, 0, 0)
    else:
        print(ans)
