from bisect import bisect_left


def has(A,x):
    b = bisect_left(A,x)
    return b < len(A) and A[b] == x


for t in range(int(input())):
    n, p =map(int, input().split())
    a = list(map(int, input().split()))
    A = sorted(list(set(a)))
    if len(A) < p:   
        i = 1
        flip = 1
        while i<n:
            if a[n-1-i]+1 <p:
                flip = a[n-1-i]+1
                break
            i += 1
        L = a[-1]
        N = (L-1)%p
        while has(A,N):
            N = (N-1)%p
        M = (L-1)%p     
        z = 0
        while True:
            if has(A,M):
                M = (M-1)%p
            elif (not z) and flip == M:
                z = flip
                M = (M-1)%p
            else:
                break
        if L > M:
            ans = (M+p-L)
        elif z:
            ans = p-L
        else:
            ans = N-L
        print('debug', L, M, N, z, flip)
    else:
        ans = 0
    print(ans)