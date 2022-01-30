for t in range(int(input())):
    n = input()
    if int(n)%2==0:
        print(0)
    else:
        if int(n[0])%2==0:
            print(1)
        else:
            even = False
            for c in n:
                if int(c)%2==0:
                    even=True
                    break
            if even:
                print(2)
            else:
                print(-1)
