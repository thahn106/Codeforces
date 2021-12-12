for t in range(int(input())):
    A,B = [int(x) for x in input().split()]
    if B==1:
        print("NO")
    else:
        print("YES")
        print("{} {} {}".format(A, A*B, A*(B+1)))
