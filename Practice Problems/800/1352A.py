for t in range(int(input())):
    n = input()
    ans = []
    l = len(n)-1
    for i in n:
        temp = int(i)* (10**l)
        l-=1
        if temp:
            ans.append(temp)
    print(len(ans))
    print(*ans)
