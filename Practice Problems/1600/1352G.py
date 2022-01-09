for t in range(int(input())):
    n = int(input())
    if n == 2 or n == 3:
        print(-1)
    else:
        ans = []
        d,r = divmod(n,4)
        if r ==0:
            sol = [2,4,1,3]
            for i in range(d):
                for c in sol:
                    ans.append(c+4*i)
        elif r == 1:
            ans.append(1)
            sol = [2,4,1,3]
            for i in range(d):
                for c in sol:
                    ans.append(1+c+4*i)
        elif r == 2:
            ans += [1,3,5,2,4,6]
            sol = [2,4,1,3]
            for i in range(d-1):
                for c in sol:
                    ans.append(6+c+4*i)
        elif r == 3:
            ans += [2,6,4,1,3,5,7]
            sol = [2,4,1,3]
            for i in range(d-1):
                for c in sol:
                    ans.append(7+c+4*i)
        print(*ans)
