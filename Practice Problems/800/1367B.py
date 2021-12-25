for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    even = 0
    odd = 0
    for i in range(n):
        if i%2:
            if not a[i]%2:
                odd +=1
        else:
            if a[i]%2:
                even+=1
    if odd ==even:
        print(odd)
    else:
        print(-1)
