for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a):
        print("YES")
    else:
        print("NO")
