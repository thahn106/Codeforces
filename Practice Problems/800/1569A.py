for t in range(int(input())):
    n = int(input())
    s = input()
    found = False
    for i in range(n-1):
        if s[i]!=s[i+1]:
            print("{} {}".format(i+1,i+2))
            found = True
            break
    if not found:
        print("-1 -1")
