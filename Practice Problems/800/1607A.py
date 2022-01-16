for t in range(int(input())):
    k = input()
    l = [0 for i in range(26)]
    for i in range(26):
        l[ord(k[i])-97]=i
    s = input()

    c = l[ord(s[0])-97]
    ans = 0
    for i in s[1:]:
        d = l[ord(i)-97]
        ans += abs(c-d)
        c = d
    print(ans)
