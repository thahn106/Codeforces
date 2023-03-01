from math import gcd


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(a[i], a[j]) <= 2:
                return "Yes"
    return "No"


for t in range(int(input())):
    print(solve())
