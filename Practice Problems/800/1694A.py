for t in range(int(input())):
    a, b = map(int, input().split())
    if a>=b:
        print('01'*b+'0'*(a-b))
    else:
        print('10'*a+'1'*(b-a))
