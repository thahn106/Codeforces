for t in range(int(input())):
    a,b = [int(x) for x in input().split()]
    n = abs(a-b)
    print(n//10+(n%10>0))
