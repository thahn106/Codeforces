for q in range(int(input())):
    n = int(input())
    ans = 0
    while n%2==0:
        ans += 1
        n = n//2
    while n%3==0:
        ans += 2
        n = n//3
    while n%5==0:
        ans += 3
        n = n//5
    if n>1:
        print(-1)
    else:
        print(ans)
