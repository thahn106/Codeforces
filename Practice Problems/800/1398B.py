for t in range(int(input())):
    s = input()
    a = []
    run = 0
    for c in s:
        if c == "1":
            run += 1
        else:
            a.append(run)
            run = 0
    a.append(run)
    a.sort(reverse=True)
    print(sum(a[0::2]))
