for t in range(int(input())):
    n = int(input())
    if (n//2)%2:
        print("NO")
    else:
        print("YES")
        ans  = []
        for i in range(n//2):
            ans.append((i+1)*2)
        for i in range(n//2):
            ans.append((i)*2+1)
        ans[-1]+=(n//2)
        print(*ans)
