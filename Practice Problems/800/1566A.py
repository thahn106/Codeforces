for t in range(int(input())):
    n,s = map(int,input().split())
    d = (n-1)//2
    print(s//(n-d))
