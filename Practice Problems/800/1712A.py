for t in range(int(input())):
    n, k = map(int, input().split())
    ans = 0
    for i in list(map(int, input().split()))[:k]:
        if i > k: ans+=1
    print(ans)