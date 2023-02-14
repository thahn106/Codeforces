for t in range(int(input())):
    n = int(input())
    s = input()
    if n % 3 == 2:
        print("NO")
        continue
    i = 1
    while i < n:
        if s[i] != s[i + 1]:
            print("NO")
            break
        i += 3
    else:
        print("YES")
