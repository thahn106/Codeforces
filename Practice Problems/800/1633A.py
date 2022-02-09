for t in range(int(input())):
    n = input()
    r = int(n)%7
    if r==0:
        print(n)
    else:
        if int(n[-1])>r:
            print(int(n)-r)
        else:
            print(int(n)+(7-r))
