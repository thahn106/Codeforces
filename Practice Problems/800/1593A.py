for t in range(int(input())):
    a = list(map(int,input().split()))
    for i in a:
        if i == max(a):
            if i == sorted(a)[1]:
                print(1)
            else:
                print(0)
        else:
            print(max(a)-i+1)
