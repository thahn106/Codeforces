n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
px = [0] * (n + 1)
qx = [0] * (n + 1)
for i, c in enumerate(p):
    px[c] = i + 1
for i, c in enumerate(q):
    qx[c] = i + 1

ans = 1
lp = n
rp = 1
lq = n
rq = 1
for i in range(1, n):
    lp = min(lp, px[i])
    rp = max(rp, px[i])
    lq = min(lq, qx[i])
    rq = max(rq, qx[i])

    if px[i + 1] < lp:
        lp_min = px[i + 1] + 1
        rp_max = n
    else:
        lp_min = 1
        rp_max = px[i + 1] - 1
    if qx[i + 1] < lq:
        lq_min = qx[i + 1] + 1
        rq_max = n
    else:
        lq_min = 1
        rq_max = qx[i + 1] - 1
    ans += max(min(lp, lq) - max(lp_min, lq_min) + 1, 0) * max(
        min(rp_max, rq_max) - max(rp, rq) + 1, 0
    )
ans += (min(px[1], qx[1]) * (min(px[1], qx[1]) - 1)) // 2
ans += ((n - max(px[1], qx[1])) * (n - max(px[1], qx[1]) + 1)) // 2
ans += (abs(px[1] - qx[1]) * (abs(px[1] - qx[1]) - 1)) // 2
print(ans)
