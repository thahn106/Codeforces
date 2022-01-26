for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    counts = [0 for i in range(n+1)]
    for i in a:
        counts[i]+=1

    ans = -1
    for i in range(n+1):
        if counts[i]==1:
            ans = i
            break

    for i in range(n):
        if a[i] == ans:
            ans = i+1
            break
    print(ans)
