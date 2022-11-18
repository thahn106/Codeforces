for t in range(int(input())):
    n, H = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    ANS = []
    for run in range(3):
        h = H
        s = [2+(run==i) for i in range(3)]
        i = 0
        ans = 0
        for p in a:
            if p>=h:
                while i<3:
                    h *= s[i]
                    i += 1
                    if p<h:
                        break
            if p>=h:
                break
            ans +=1
            h += p//2
        
        ANS.append(ans)
    print(max(ANS))
