for t in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    last = 0
    s = set()
    for i in x:
        if i in s:
            s.add(i+1)
        else:
            s.add(i)
    print(len(s))
