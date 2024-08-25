import sys

from math import isqrt

input = sys.stdin.readline


def nonemin(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


def tri(n):
    if n <= 0:
        return 0
    return n * (n + 1) // 2


def cnt(iset):
    # print(f"{iset=}")

    if len(iset) == 2:
        return (iset[0] + 1) * (iset[1] + 1)

    m = min(iset[1:-1])
    m = min(m, iset[0] + iset[-1])
    return tri(m + 1) - tri(m - iset[0]) - tri(m - iset[-1])


def verify(iset, k):
    # print(f"verifying {k=}")
    assert (len(iset) - 1) % k == 0
    new_iset = [iset[0]]
    for i in range(k + 1, len(iset) - 1, k):
        if iset[i : i + k - 1] != iset[1 : 1 + k - 1]:
            return 0
        new_iset.append(iset[i - 1])
    new_iset.append(iset[-1])
    return cnt(new_iset)


for t in range(int(input())):
    s = input().strip()
    start = -1
    for i in range(len(s)):
        if s[i] == "a":
            continue
        else:
            start = i
            break
    # all a's
    if start == -1:
        print(len(s) - 1)
        continue
    end = start
    last_end = start
    iset = []
    ind = 0
    cur_interval = 0
    k = start + 1
    while k <= len(s):
        if k == len(s):
            if ind:
                k = end + 1
                end = k
                last_end = k
                iset = []
                ind = 0
                cur_interval = 0
                continue
            else:
                break
        elif s[k] == s[start + ind]:
            if ind == 0:
                iset.append(cur_interval)
                cur_interval = 0
            ind += 1
            if ind == end - start + 1:
                last_end = k
                ind = 0
        elif ind == 0 and s[k] == "a":
            cur_interval += 1
        else:
            k = end + 1
            end = k
            last_end = k
            iset = []
            ind = 0
            cur_interval = 0
        k += 1

    iset = [start] + iset + [len(s) - last_end - 1]
    ans = 0
    pat_cnt = len(iset) - 1

    # print(f"{iset=}")
    # print(f"{pat_cnt=}")
    # print(f"pat={s[start:end+1]}")

    for i in range(1, pat_cnt + 1):
        if i * i > pat_cnt:
            break
        d, r = divmod(pat_cnt, i)
        if r != 0:
            continue
        ans += verify(iset, i)
        if i != d:
            ans += verify(iset, d)

    print(ans)
