for t in range(int(input())):
    n = int(input())
    s = input()
    first = n
    for i, c in enumerate(s):
        if c == '8':
            first = i
            break
    if n-i >= 11:
        print("YES")
    else:
        print("NO")
