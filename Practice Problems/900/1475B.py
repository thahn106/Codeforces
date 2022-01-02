for t in range(int(input())):
    n = int(input())
    q,r =  divmod(n,2020)
    if r>q:
        print("NO")
    else:
        print("YES")
