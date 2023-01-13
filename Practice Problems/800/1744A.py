for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    c = [""]*51
    ans = "YES"
    for i,k in enumerate(a):
        if not c[k]:
            c[k] = s[i]
        elif c[k] != s[i]:
            ans ="NO"
            break
    print(ans)