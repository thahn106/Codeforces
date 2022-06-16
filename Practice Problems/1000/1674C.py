for q in range(int(input())):
    s = len(input())
    t = input()
    if 'a' not in t:
        print(2**s)
    elif t == 'a':
        print(1)
    else:
        print(-1)
