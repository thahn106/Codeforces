for t in range(int(input())):
    n = int(input())
    s = input()
    i = n - 1
    ans = ""
    while i >= 0:
        if s[i] == "0":
            v = s[i - 2 : i]
            i -= 3
        else:
            v = s[i]
            i -= 1
        ans += chr(ord("a") - 1 + int(v))

    print(ans[::-1])
