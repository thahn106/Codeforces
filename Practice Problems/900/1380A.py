for t in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    a, b, c = 0, 0, 0
    for i, k in enumerate(p):
        if not i:
            a = i
        else:
            if not b:
                if k > p[i - 1]:
                    b = i
                else:
                    a = i
            else:
                if k > p[i - 1]:
                    b = i
                else:
                    c = i
                    print("YES")
                    print(a + 1, b + 1, c + 1)
                    break
    if not c:
        print("NO")
