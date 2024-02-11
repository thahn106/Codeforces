import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    start = a[0]
    end = a[0] + n - 1
    start_ptr = 0
    end_ptr = 0
    ans = 1
    cur = 1
    cv = a[0]
    while end_ptr < n:
        if a[end_ptr] <= end:
            if cv != a[end_ptr]:
                cur += 1
                cv = a[end_ptr]
            end_ptr += 1
            ans = max(ans, cur)
            continue

        start_val = a[start_ptr]
        while start_ptr < n and a[start_ptr] == start_val:
            start_ptr += 1
        cur -= 1
        start = a[start_ptr]
        end = a[start_ptr] + n - 1
    print(ans)
    # print(f"ans: {ans}")
