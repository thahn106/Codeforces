for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    d = [b[i]-a[i] for i in range(n)]
    start = False
    end = False
    working = True
    amount = 0
    for c in d:
        if c > 0:
            if not start:
                start = True
                amount = c
            elif end:
                working= False
                break
            else:
                if amount != c:
                    working = False
                    break
        elif c<0:
            working = False
            break
        else:
            if start: end = True
    if working:
        print("YES")
    else:
        print("NO")
