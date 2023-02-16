for t in range(int(input())):
    r, s = map(int, input().split())
    a = input() + input()[::-1]
    count = 0
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            count += 1
    if count <= 1:
        print("YES")
    else:
        print("NO")
