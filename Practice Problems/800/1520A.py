for t in range(int(input())):
    n = int(input())
    s = input()
    a = [False for i in range(26)]
    cur = ""
    possible = True
    for c in s:
        if c != cur:
            if a[ord(c)-65]:
                possible=False
            else:
                a[ord(c)-65] = True
        cur = c
    if possible:
        print("YES")
    else:
        print("NO")
