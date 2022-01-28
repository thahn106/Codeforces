for t in range(int(input())):
    n = int(input())
    if n>30:
        print("YES")
        if n ==36:
            print("5 6 10 15")
        elif n ==40:
            print("9 6 10 15")
        elif n ==44:
            print("13 6 10 15")
        else:
            print("{} 6 10 14".format(n-30))
    else:
        print("NO")
