for t in range(int(input())):
    n = int(input())
    s = input()
    ans = n - 1
    for i in range(n - 2):
        if s[i] == s[i + 2]:
            ans -= 1
    print(ans)
