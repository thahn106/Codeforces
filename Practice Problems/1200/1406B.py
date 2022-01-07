for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if max(a)<0:
        ans = a[-5]*a[-4]*a[-3]*a[-2]*a[-1]
    else:
        a.sort(key = abs)
        # print(a)
        ans = a[-5]*a[-4]*a[-3]*a[-2]*a[-1]
        for i in range(5):
            temp = 1
            for j in range(5):
                if not i==j:
                    temp *= a[-(j+1)]
            # print("i:{} temp:{}".format(i,temp))
            for j in a[:-5]:
                ans = max(ans, temp*j)
    print(ans)
