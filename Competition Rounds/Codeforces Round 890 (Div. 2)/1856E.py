import sys

sys.setrecursionlimit(1000050)

N = int(input())
a = list(map(int, input().split()))

children = [[] for _ in range(N)]


for i in range(N-1):
    children[a[i]-1].append(i+1)



def minDifference(arr):
    n = len(arr)
    sum = 0
    for i in range(n):
        sum += arr[i]
    y = sum // 2 + 1
    dp = [False for i in range(y)]
    dd = [False for i in range(y)]

    dp[0] = True
    for i in range(n):
        for j in range(y):
            if (j + arr[i] < y and dp[j]):
                dd[j + arr[i]] = True
        for j in range(y):
            if (dd[j]):
                dp[j] = True
            dd[j] = False 
    for i in range(y-1, 0, -1):
        if (dp[i]):
            return (sum - i) * i
    return (sum//2)**2


def optimize(N):
    ans = 0
    count = 1
    sizes = []
    for child in children[N]:
        tmp, tmp_count = optimize(child)
        sizes.append(tmp_count)
        ans += tmp
        count += tmp_count
    ans += minDifference(sizes)
    return ans, count

ans, count = optimize(0)
print(ans)
