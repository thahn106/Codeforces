for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    for i in range(n):
        if a[i] == m:
            print(i+1)
            break
