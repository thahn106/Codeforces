for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    o = 0
    for i in a:
        if i%2:
            o +=1 
    print(min(o, n-o))
