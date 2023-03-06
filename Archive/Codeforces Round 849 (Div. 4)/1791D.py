def f(flist):
    ans = 0
    for i in flist:
        if i:
            ans += 1
    return ans


def i(c):
    return ord(c) - 97


for t in range(int(input())):
    n = int(input())
    s = input()
    ans = 0
    a = [0] * 26
    b = [0] * 26
    for c in s:
        b[i(c)] += 1

    for c in s:
        a[i(c)] += 1
        b[i(c)] -= 1
        ans = max(ans, f(a) + f(b))
    print(ans)
