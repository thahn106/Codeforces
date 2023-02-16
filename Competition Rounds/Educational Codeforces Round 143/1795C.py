from bisect import bisect_right

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dp = [0]
    for i in b:
        dp.append(dp[-1] + i)
    ref = []
    run = 0
    ops = []
    # print(*dp)
    for i, c in enumerate(a):
        ind = bisect_right(dp, c + run)
        # print(f"{c + run=}, {ind=}")
        ops.append((ind - 1, c + run - dp[ind - 1]))
        run += b[i]
    ops.sort()
    # print(*ops)

    cur = 0
    op_ind = 0
    ans = []
    for i in range(n):
        cur += 1
        temp = 0
        while op_ind < n and ops[op_ind][0] == i:
            cur -= 1
            temp += ops[op_ind][1]
            op_ind += 1
        # print(f"{i=}, {cur=}, {temp=}")
        temp += cur * b[i]
        ans.append(temp)
    print(*ans)
