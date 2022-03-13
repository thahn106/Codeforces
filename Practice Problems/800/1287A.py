for t in range(int(input())):
    k = int(input())
    s = input()
    ans = 0
    last = -1
    for i,c in enumerate(s):
        if c =='A':
            last = i
        else:
            if last != -1:
                ans = max(ans, i-last)
    print(ans)
