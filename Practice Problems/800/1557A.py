for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    print(sum(a[:-1])/(n-1)+a[-1])
