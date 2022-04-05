for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.append(0)
    a.sort(reverse = True)
    if a[0]>a[1]+1:
        print("NO")
    else:
        print("YES")
