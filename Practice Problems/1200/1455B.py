for t in range(int(input())):
    x = int(input())
    ans = 0
    while ans*(ans+1)//2 < x:
        ans+=1
    if ans*(ans+1)//2 == x+1:
        ans +=1
    print(ans)
