for t in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))
    found = False
    for i,c in enumerate(p):
        if not found:
            if c != i+1:
                found = True
                start = i
        else:
            if c == start+1:
                end = i
    if found:
        p[start:end+1] = p[start:end+1][::-1]
    print(*p)
