for t in range(int(input())):
    n = int(input())
    b = input()
    last = 0
    ans = ""
    for c in b:
        if int(c)+1==last:
            last = int(c)
            ans += "0"
        else:
            last = int(c)+1
            ans += "1"
    print(ans)
