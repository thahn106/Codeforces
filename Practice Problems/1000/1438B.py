for t in range(int(input())):
    n = int(input())
    b = list(map(int,input().split()))
    if len(set(b))==n:
        print("NO")
    else:
        print("YES")
