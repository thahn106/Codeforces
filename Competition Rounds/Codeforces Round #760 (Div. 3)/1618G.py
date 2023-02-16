import sys
from bisect import bisect_left

input = sys.stdin.readline


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i == len(a):
        return i - 1
    elif i == 0 or a[i] == x:
        return i
    else:
        return i - 1


n, m, q = map(int, input().split())


items = []
cur = 0
for c in input().split():
    items.append((int(c), 1))
    cur += int(c)
for c in input().split():
    items.append((int(c), 0))

items.sort()

dp_items = [0]
dp_own = [0]
for price, own in items:
    dp_items.append(dp_items[-1] + price)
    dp_own.append(dp_own[-1] + own)


difs = {}
for i in range(1, n + m):
    d = items[i][0] - items[i - 1][0]
    if d in difs:
        difs[d].append(i)
    else:
        difs[d] = [i]

segments = {}
prev = {}
for i in range(n + m):
    segments[i] = i + 1
    prev[i + 1] = i


def val(start, end):
    cnt = dp_own[end] - dp_own[start]
    return dp_items[end] - dp_items[end - cnt]


keys = list(difs)
keys.sort()

dlist = [0]
ans = [cur]
for key in keys:
    arr = difs[key]
    for bp in arr:
        # join start-bp with bp-end
        start = prev[bp]
        end = segments[bp]
        cur -= val(start, bp)
        cur -= val(bp, end)
        cur += val(start, end)
        prev[end] = start
        segments[start] = end
        del prev[bp]
        del segments[bp]
    dlist.append(key)
    ans.append(cur)

for q in list(map(int, input().split())):
    i = BinarySearch(dlist, q)
    sys.stdout.write(str(ans[i]) + "\n")
