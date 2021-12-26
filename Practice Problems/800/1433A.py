for t in range(int(input())):
    x = input()
    s = len(x)
    ans = (int(x[0])-1)*10+((s*(s+1))//2)
    print(ans)
