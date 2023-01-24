for t in range(int(input())):
    n = int(input())
    a = [(int(c), i)  for i, c in enumerate(input().split())]
    a.sort()
    ans = n
    start = 0
    for i in range(1, n):
        if a[i][1] < a[i-1][1]:
            ans = min(ans, max(start, n-i))
            start = i
    ans = min(ans, max(start, 0))
    print(ans)