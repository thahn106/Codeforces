for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(n):
        a[i],b[i] = min(a[i],b[i]),max(a[i],b[i])
    print(max(a)*max(b))
