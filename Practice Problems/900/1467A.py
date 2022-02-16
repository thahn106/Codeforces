for t in range(int(input())):
    n = int(input())
    ans = [0]*n
    for i in range(n):
        ans[i]=str((8+abs(-1+i))%10)
    print("".join(ans))
