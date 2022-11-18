for t in range(int(input())):
    s = input()
    ans = "YES"
    if s[0] == 'Y':
        os = 0
    elif s[0] == 'e':
        os = 1
    elif s[0] == 's':
        os = 2
    else:
        os = -1
    if ans == "YES":
        for i,c in enumerate(s):
            if c != 'Yes'[(i+os)%3]:
                ans = "NO"
                break
    print(ans)
