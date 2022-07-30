for t in range(int(input())):
    x = int(input())
    a = list(map(int,input().split()))
    count=0
    while x:
        x = a[x-1]
        count+=1
    if count == 3:
        print("YES")
    else:
        print("NO")
