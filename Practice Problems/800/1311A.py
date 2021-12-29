for t in range(int(input())):
    a,b = map(int,input().split())
    if a == b:
        ans = 0
    elif a < b and (a-b)%2==0:
        ans = 2
    elif a > b and (a-b)%2:
        ans = 2
    else:
        ans = 1
    print(ans)
