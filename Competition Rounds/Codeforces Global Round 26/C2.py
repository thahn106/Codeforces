import sys

input = sys.stdin.readline
MOD = 998244353

for t in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    ma = 0
    mi = 0
    mac = 1
    mic = 1
    for v in x:
        if ma == mi:
            a = [ma + v, abs(ma + v)]
            b = [mac, mac]
        else:
            a = [ma + v, mi + v, abs(ma + v), abs(mi + v)]
            b = [mac, mic, mac, mic]
        ma = max(a)
        mi = min(a)
        new_mac = 0
        new_mic = 0
        for res, cnt in zip(a, b):
            if res == ma:
                new_mac += cnt
            if res == mi:
                new_mic += cnt

        mac = new_mac % MOD
        mic = new_mic % MOD

    print(mac)
