for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    count = [0]*101
    for i in a:
        d = abs(i)
        if d:
            count[d]=min(2, count[d]+1)
        else:
            count[d]=1
    print(sum(count))
