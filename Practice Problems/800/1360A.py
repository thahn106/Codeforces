for t in range(int(input())):
    a,b = map(int, input().split())
    print(max(a,b,min(a,b)*2)**2)
