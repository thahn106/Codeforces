for t in range(int(input())):
    n = int(input())
    S = list(map(int,input().split()))
    S.sort()
    found =False
    for i in range(1,1025):
        if S ==  sorted([c^i for c in S]):
            found = True
            print(i)
            break
    if not found:
        print(-1)
