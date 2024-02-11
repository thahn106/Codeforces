import sys

input = sys.stdin.readline

for t in range(int(input())):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    if a == b:
        if a % 2 == 0:
            print("Yes")
        else:
            print("No")
        continue
    if b % 2 == 0:
        if a * 2 != b:
            print("Yes")
            continue
    if a % 2 == 0:
        print("Yes")
    else:
        print("No")
