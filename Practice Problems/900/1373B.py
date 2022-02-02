for t in range(int(input())):
    s = input()
    o = 0
    for c in s:
        if int(c): o+=1
    d = min(o,len(s)-o)
    if d%2:
        print("DA")
    else:
        print("NET")
