import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    mons = [(abs(x), h) for h, x in zip(a, x)]
    mons.sort()

    possible = True
    cur = 0
    shots = 0
    for x, h in mons:
        if x > cur:
            shots += (x - cur) * k
            cur = x
        if h > shots:
            possible = False
            break
        shots -= h

    ans = "YES" if possible else "NO"
    sys.stdout.write(f"{ans}\n")
