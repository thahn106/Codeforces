for t in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    a = []
    for i in range(n-1):
        for j in range(i+1,n):
            a.append(x[j]-x[i])
    print(len(set(a)))
