for t in range(int(input())):
    a,b,c = map(int, input().split())
    A = (a-1)
    B = abs(b-c)+abs(c-1)
    if A<B:
        print(1)
    elif B<A:
        print(2)
    else:
        print(3)