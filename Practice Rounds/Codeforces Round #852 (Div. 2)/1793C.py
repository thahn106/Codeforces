for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    x = 1
    j = n - 1
    y = n
    while i < j:
        if a[i] == x:
            i += 1
            x += 1
        elif a[i] == y:
            i += 1
            y -= 1
        elif a[j] == x:
            j -= 1
            x += 1
        elif a[j] == y:
            j -= 1
            y -= 1
        else:
            break
    if i < j:
        print(i + 1, j + 1)
    else:
        print(-1)
