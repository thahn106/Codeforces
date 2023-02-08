for t in range(int(input())):
    n = int(input())
    s = input()
    i = 0
    while i < n // 2:
        if s[i] != s[n - 1 - i]:
            i += 1
        else:
            break
    print(n - 2 * i)
