for t in range(int(input())):
    n = int(input())
    if n%2050:
        print(-1)
    else:
        print(sum(list(map(int,list(str(n//2050))))))
