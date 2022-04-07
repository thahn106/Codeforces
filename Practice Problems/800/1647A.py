for t in range(int(input())):
    n = int(input())
    d,r = divmod(n,3)
    if r==0:
        print('21'*d)
    elif r == 1:
        print('12'*d+'1')
    else:
        print('21'*d+'2')
