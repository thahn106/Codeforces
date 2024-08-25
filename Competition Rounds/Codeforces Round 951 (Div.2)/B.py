import sys

input = sys.stdin.readline

for t in range(int(input())):
    x, y = map(int, input().split())
    if x < y:
        x, y = y, x
    x = bin(x)[2:][::-1]
    y = bin(y)[2:][::-1]
    if len(y) < len(x):
        y += "0" * (len(x) - len(y))
    i = 0
    ans = 1
    while i < len(x) and i < len(y):
        if x[i] == y[i]:
            ans *= 2
        else:
            break
        i += 1

    print(ans)
