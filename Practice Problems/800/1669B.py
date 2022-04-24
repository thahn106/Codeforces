for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    counts = [0] * (n+1)
    for i in a:
        counts[i] += 1
        found = False
    for i in range(n+1):
        if counts[i] >= 3:
            found = True
            print(i)
            break
    if not found:
        print(-1)
