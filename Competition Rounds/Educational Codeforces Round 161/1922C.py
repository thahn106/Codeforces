import sys

input = sys.stdin.readline


for t in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    forward = [0] * (N)
    backward = [0] * (N)

    for i in range(N):
        if i == 0:
            forward[i] = 1
        elif i == N - 1:
            backward[i] = 1
        else:
            fd = a[i + 1] - a[i]
            bd = a[i] - a[i - 1]
            if fd > bd:
                forward[i] = fd
                backward[i] = 1
            elif fd < bd:
                forward[i] = 1
                backward[i] = bd

    dp_forward = [0] * (N)
    cur = 0
    for i in range(N - 1):
        cur += forward[i]
        dp_forward[i + 1] = cur

    dp_backwards = [0] * (N)
    cur = 0
    for i in range(N - 1, 0, -1):
        cur += backward[i]
        dp_backwards[i - 1] = cur

    for _ in range(m):
        fr, to = map(int, input().split())
        fr -= 1
        to -= 1
        if fr < to:
            ans = dp_forward[to] - dp_forward[fr]
        elif fr > to:
            ans = dp_backwards[to] - dp_backwards[fr]
        else:
            ans = 0

        sys.stdout.write(str(ans) + "\n")
