for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    if s % n == 0 and s // n in a:
        print("YES")
    else:
        print("NO")
