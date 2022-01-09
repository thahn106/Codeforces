for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    mods = [0 for i in range(n)]
    for i in range(n):
        mods[(i+a[i])%n]+=1
    if max(mods)==1:
        print("YES")
    else:
        print("NO")
