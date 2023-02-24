for t in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    if not k:
        print("YES")
    else:
        s1 = s[:k]
        s2 = s[-k:][::-1]
        if n > 2 * k and s1 == s2:
            print("YES")
        else:
            print("NO")
