import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, k = map(int, input().split())
    s = list(map(int, input().strip()))
    d = n // k
    needed = [(d // 2) * k, ((d + 1) // 2) * k]
    ones, zeros = 0, 0
    for c in s:
        if c == 1:
            ones += 1
        else:
            zeros += 1

    if s[0] == 0:
        end = 0
        if d % 2:
            start = 0
        else:
            start = 1
        needed[0], needed[1] = needed[1], needed[0]
    else:
        end = 1
        if d % 2:
            start = 1
        else:
            start = 0

    # print(start, end, needed)

    if ones != needed[1] or zeros != needed[0]:
        sys.stdout.write("-1\n")
        continue

    ans = 0
    end_found = False
    possible = True
    for i in range(n):
        d = i // k
        if d % 2:
            expected = 1 - end
        else:
            expected = end
        # print(i, d, s[i], expected)
        if s[i] == expected:
            ans = i + 1
        else:
            break

    first_block = True
    start_pos = n
    cur = None
    block_size = 0
    for i in range(n - 1, -1, -1):
        if cur is None:
            cur = s[i]
        if s[i] == cur:
            block_size += 1
            if block_size == k:
                block_size = 0
                first_block = False
                cur = 1 - cur
                if s[i] == start:
                    start_pos = i
            if first_block and s[i] == start:
                start_pos = i
        else:
            if first_block:
                cur = 1 - cur
                block_size = 1
                first_block = False
            else:
                break

    # print(ans, start_pos)
    if ans >= start_pos:
        if ans != n:
            ans = start_pos
    else:
        ans = 0

    if ans:
        sys.stdout.write(str(ans) + "\n")
    else:
        sys.stdout.write("-1\n")
