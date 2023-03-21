for t in range(int(input())):
    s = input()
    p = int(input())
    chars = []
    total = 0
    for i, c in enumerate(s):
        v = ord(c) - 96
        chars.append((v, i, c))
        total += v
    chars.sort(reverse=True)
    nc = []
    for v, i, c in chars:
        if total > p:
            total -= v
        else:
            nc.append((i, c))
    nc.sort()
    ans = [c for i, c in nc]
    print("".join(ans))
