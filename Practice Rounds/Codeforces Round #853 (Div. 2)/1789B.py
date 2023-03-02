for t in range(int(input())):
    n = int(input())
    s = input()
    status = 0
    pos = True
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            if status == 0:
                status = 1
            elif status == 2:
                pos = False
                break
        else:
            if status == 1:
                status = 2
    if pos:
        print("YES")
    else:
        print("NO")
