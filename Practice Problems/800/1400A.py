for t in range(int(input())):
    n = int(input())
    s = input()
    ans = ""
    for i in range(n):
        ans += s[i:][i]
    print(ans)
