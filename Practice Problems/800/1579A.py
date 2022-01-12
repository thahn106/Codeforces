for t in range(int(input())):
    s = input()
    cc = [0,0,0]
    for c in s:
        cc[ord(c)-65]+=1
    if cc[0]+cc[2] == cc[1]:
        print("YES")
    else:
        print("NO")
