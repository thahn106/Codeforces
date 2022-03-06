for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if sorted(a) == a[::-1] and len(a)==len(set(a)):
        print("NO")
    else:
        print("YES")
