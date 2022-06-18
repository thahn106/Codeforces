for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    if max(a) >= max(b):
        print('Alice')
    else:
        print('Bob')
    if max(b) >= max(a):
        print('Bob')
    else:
        print('Alice')
