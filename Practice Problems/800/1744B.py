import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    even, odd = 0, 0
    for i in a:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    s = sum(a)
    for _ in range(q):
        type, x = map(int, input().split())
        if type == 1:
            s += x * (odd)
            if x % 2:
                even += odd
                odd = 0
        else:
            s += x * (even)
            if x % 2:
                odd += even
                even = 0
        sys.stdout.write(str(s) + "\n")
