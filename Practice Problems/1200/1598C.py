for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    ref = {}
    for c in a:
        if c in ref:
            ref[c] += 1
        else:
            ref[c] = 1
        s += c
    s *= 2
    if s % n:
        print(0)
        continue
    s //= n
    ans = 0
    for key, val in ref.items():
        if s - key == key:
            ans += val * (val - 1) // 2
        elif s - key > key and (s - key) in ref:
            ans += val * ref[s - key]
    print(ans)
