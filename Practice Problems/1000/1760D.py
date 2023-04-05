for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for c in a:
        if (not b) or c != b[-1]:
            b.append(c)
    ans = 0
    for i in range(len(b)):
        if (i == 0 or b[i - 1] >= b[i]) and (i == len(b) - 1 or b[i] <= b[i + 1]):
            ans += 1
    if ans == 1:
        print("YES")
    else:
        print("NO")
