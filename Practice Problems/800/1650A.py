for t in range(int(input())):
    s = input()
    c = input()
    found = False
    for i,ch in enumerate(s):
        if ch == c and i%2==0:
            found = True
            break
    if found: print("YES")
    else: print("NO")
