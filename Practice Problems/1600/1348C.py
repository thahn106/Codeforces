import sys
def get_ints(): return list(map(int, sys.stdin.readline().split()))
from math import floor

for t in range(int(input())):
    N,K = get_ints()
    s = [c for c in input()]
    s.sort()
    if K==N or s[K-1]!=s[0]:
        print(s[K-1])
    else:
        ans = s[0]
        if s[K]!=s[N-1]:
            ans +="".join(s[K:])
        else:
            ans += s[N-1]*floor((N-1)/K)
        print(ans)
