for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if min(a)==max(a):
        print(len(a))
    else:
        print(1)
