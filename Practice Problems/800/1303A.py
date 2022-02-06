for t in range(int(input())):
    s = input()
    ans = 0
    start = False
    run = 0
    for c in s:
        if int(c):
            start = True
            ans += run
            run = 0
        else:
            if start:
                run+=1
    print(ans)
