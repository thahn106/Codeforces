for t in range(int(input())):
    n = int(input())
    if n%2:
        d = (n-3)//2
        print("7"+"1"*d)
    else:
        d = n//2
        print("1"*d)
