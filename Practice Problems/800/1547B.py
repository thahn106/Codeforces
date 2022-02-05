for t in range(int(input())):
    st = input()
    i = len(st)
    s = 0
    e = i-1
    good = True
    while i:
        if st[s]==chr(i+96):
            s +=1
            i -=1
        elif st[e]==chr(i+96):
            e -=1
            i -=1
        else:
            good = False
            break
    if good:
        print("YES")
    else:
        print("NO")
