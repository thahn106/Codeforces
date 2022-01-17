for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if sum(a)%n:
        print(-1)
    else:
        d = sum(a)//n
        print(sum([int(i-d)>0 for i in a]))
