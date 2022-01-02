for t in range(int(input())):
    n = int(input())
    for k in range(2,30):
        x, d = divmod(n , 2**k-1)
        if d ==0:
            ans = x
    print(ans)
