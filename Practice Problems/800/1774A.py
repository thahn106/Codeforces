for t in range(int(input())):
    n = int(input())
    cur = 0
    ans = ""
    for i,c in enumerate(input()):
        if i:
            if int(c):
                if cur:
                    ans += '-'
                    cur = 0
                else:
                    ans += '+'
                    cur = 1
            else:
                ans += '+'
        else:
            cur = int(c)
    print(ans)