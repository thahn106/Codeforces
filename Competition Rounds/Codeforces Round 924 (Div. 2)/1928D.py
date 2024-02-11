import sys

from math import ceil


input = sys.stdin.readline


def power(count, squads):
    if squads == 1:
        ans = 0
    if squads >= count:
        ans = (count * (count - 1)) // 2
    else:
        r, d = divmod(count, squads)
        # d squads will have r + 1 members
        # squads - d squads will have r members
        ans = ((squads - d) * (count - r) * r + d * (count - r - 1) * (r + 1)) // 2
    # print("DEBUG POWER", count, squads, ans)
    return ans


for t in range(int(input())):
    n, b, x = map(int, input().split())
    c = list(map(int, input().split()))
    incs = ceil(x / b)

    def test(squads):
        ans = -(squads - 1) * x
        for species in c:
            ans += b * power(species, squads)
        return ans

    l = 1
    r = max(c)
    l_val = test(1)
    r_val = test(max(c))
    while l + 2 < r:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3
        m1_val = test(m1)
        m2_val = test(m2)
        if m1_val <= m2_val:
            l = m1
            l_val = m1_val
        else:
            r = m2
            r_val = m2_val
    ans = max(map(test, range(l, r + 1)))
    print(ans)
