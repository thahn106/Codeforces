for i in range(int(input())):
    s = input()
    ans = ord(s[1])-ord('a')
    if ord(s[1])<ord(s[0]):
        ans += 1
    ans += 25*(ord(s[0])-ord('a'))
    print(ans)
