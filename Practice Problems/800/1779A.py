for t in range(int(input())):
    n = int(input())
    s = input()
    if 'RL' in s:
        print(0)
    else:
        f = False
        for i in range(n-1):
            if s[i:i+2] == 'LR':
                print(i+1)
                f = True
        if not f:
            print(-1)

