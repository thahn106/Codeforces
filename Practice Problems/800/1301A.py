for t in range(int(input())):
    a = input()
    b = input()
    c = input()
    working = True
    for i in range(len(a)):
        if not (a[i]==c[i] or b[i]==c[i]):
            working = False
            break
    if working:
        print("YES")
    else:
        print("NO")
