for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = "YES"
    for i in a[1:]:
        if i%a[0]:
            ans = "NO"
    print(ans)