for t in range(int(input())):
    s = input()
    l = len(s)//2
    if 2*l == len(s) and s[:l]==s[l:]:
        print("YES")
    else:
        print("NO")
