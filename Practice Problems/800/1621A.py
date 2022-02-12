for t in range(int(input())):
    n,k = map(int,input().split())
    if k<= (n+1)//2:
        for i in range(n):
            row = ""
            for j in range(n):
                if i==j and i%2==0 and (i//2+1)<=k:
                    row+="R"
                else:
                    row+="."
            print(row)
    else:
        print(-1)
