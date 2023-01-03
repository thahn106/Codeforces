for t in range(int(input())):
    n = int(input())
    s = True
    for a,b in zip(input(),input()):
        if (a=='R' and b!='R') or (a!='R' and b=='R'):
            s = False
            break
    if s:
        print("YES")
    else:
        print("NO")