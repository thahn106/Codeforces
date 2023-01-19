for t in range(int(input())):
    n = int(input())
    if n < 4 or n % 2:
        print(-1)
    else:
        k = n//2
        if k % 2:
            first = 1+(k-3)//2
        else:
            first = k//2
        if k % 3 == 1:
            second = 2+(k-4)//3
        elif k % 3 == 2:
            second = 1+(k-2)//3
        else:
            second = k//3
        print(second, first)
