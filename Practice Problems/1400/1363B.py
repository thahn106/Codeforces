for t in range(int(input())):
    s = input()
    n = len(s)
    rs = []
    run = 0
    for char in s:
        run += int(char)
        rs.append(run)
    ans = n
    for i in range(n):
        ans =min(ans, min(rs[i],(i+1)-rs[i])+min((rs[-1]-rs[i]),n-(i+1)-(rs[-1]-rs[i])))
    print(ans)
