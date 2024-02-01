import sys

input = sys.stdin.readline


for t in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    cur = 0
    prev_count = 0
    cur_count = 0
    for x in a:
        if x > cur:
            if cur_count >= 3:
                ans += cur_count * (cur_count - 1) * (cur_count - 2) // 6
            if cur_count >= 2:
                ans += cur_count * (cur_count - 1) * prev_count // 2
            prev_count += cur_count
            cur = x
            cur_count = 1
        else:
            cur_count += 1
    else:
        if cur_count >= 3:
            ans += cur_count * (cur_count - 1) * (cur_count - 2) // 6
        if cur_count >= 2:
            ans += cur_count * (cur_count - 1) * prev_count // 2

    print(ans)
