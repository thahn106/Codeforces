from cmath import e


for t in range(int(input())):
    n = input()
    f5 = False
    f0 = False
    ans = 0
    for i, c in enumerate(n[::-1]):
        if c == '2':
            if f5:
                ans = i-1
                break
        elif c == '5':
            if f0:
                ans = i-1
                break
            f5 = True
        elif c == '7':
            if f5:
                ans = i-1
                break
        elif c == '0':
            if f0:
                ans = i-1
                break
            else:
                f0 = True
    print(ans)
