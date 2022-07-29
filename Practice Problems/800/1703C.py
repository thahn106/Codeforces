for T in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    for n in range(N):
        _, s =input().split()
        for c in s:
            if c =='D':
                a[n]+=1
            else:
                a[n]-=1
        a[n] = a[n] %10
    print(*a)
