for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if a[0] == 1:
        ans = [n+1]+list(range(1,n+1))
        print(*ans)
    elif a[-1]==0:
        ans = list(range(1,n+2))
        print(*ans)
    else:
        for i in range(n-1):
            if (not a[i]) and a[i+1]:
                ans = list(range(1,i+2))+[n+1]+list(range(i+2,n+1))
                print(*ans)
                break
