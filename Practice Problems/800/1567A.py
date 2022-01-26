for t in range(int(input())):
    n = int(input())
    d = input()
    ans = []
    for c in d:
        if c=="D":
            ans.append("U")
        elif c=="U":
            ans.append("D")
        else:
            ans.append(c)
    print("".join(ans))
