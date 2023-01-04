for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mina = min(a)
    maxa = max(a)
    if mina==max(a):
        print(n*(n-1))
    else:
        minc = 0
        maxc = 0
        for i in a:
            if i == mina:
                minc +=1
            if i == maxa:
                maxc += 1
        print(minc*maxc*2)
