import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [(x, y) for x, y in zip(a, b)]
    c.sort()
    for i in range(n):
        if i:
            sys.stdout.write(" ")
        sys.stdout.write(str(c[i][0]))
    sys.stdout.write("\n")
    for i in range(n):
        if i:
            sys.stdout.write(" ")
        sys.stdout.write(str(c[i][1]))
    sys.stdout.write("\n")
