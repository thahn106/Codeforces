for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        ans += (i-1)
    if ans%2:
        print("errorgorn")
    else:
        print("maomao90")
