for t in range(int(input())):
    n = int(input())
    a = 0
    for c in input():
        a = max(a, ord(c) - 96)
    print(a)
