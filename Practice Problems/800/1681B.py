for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    print(a[sum(b)%n])
