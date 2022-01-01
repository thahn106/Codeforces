for t in range(int(input())):
    s = input()
    oo = -1
    zz = -1
    for i in range(len(s)-1):
        if s[i:i+2] == "00":
            zz = i
        if s[i:i+2] == "11" and oo == -1:
            oo = i
    if oo < zz and zz >=0 and oo >=0:
        print("NO")
    else:
        print("YES")
