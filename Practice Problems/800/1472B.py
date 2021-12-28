for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = sum(a)
    if s%2 or (s%4==2 and min(a)==2):
        print("NO")
    else:
        print("YES")
