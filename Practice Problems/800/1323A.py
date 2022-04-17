for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1 and a[0]%2:
        print(-1)
    else:
        if a[0]%2:
            if a[1]%2:
                print(2)
                print(1,2)
            else:
                print(1)
                print(2)
        else:
            print(1)
            print(1)
