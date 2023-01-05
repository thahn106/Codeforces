for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ref = list(zip(a, range(n)))
    ref.sort(reverse=True)    
    p = [[0]*n, [0]*n]
    pos = True
    cur, i = n,0
    fill = []

    while cur:
        if i >= n:
            if len(fill)>1:
                r,ind = fill.pop()
                p[r][ind] = cur
                r,ind = fill.pop()
                p[r][ind] = cur
            else:
                pos = False
                break
        elif ref[i][0]<cur:
            if len(fill)>1:
                r,ind = fill.pop()
                p[r][ind] = cur
                r,ind = fill.pop()
                p[r][ind] = cur
            else:
                pos = False
                break
        elif ref[i][0] == cur:
            if i+1<n:
                if ref[i+1][0] == cur:
                    p[0][ref[i][1]] = cur
                    p[1][ref[i+1][1]] = cur
                    fill.append((1,ref[i][1]))
                    fill.append((0,ref[i+1][1]))
                    i+=2
                elif fill:
                    p[0][ref[i][1]] = cur
                    fill.append((1,ref[i][1]))
                    r,ind = fill.pop()
                    p[r][ind] = cur
                    i+=1
                else:
                    p[0][ref[i][1]] = cur
                    p[1][ref[i][1]] = cur
                    i+=1
            else:
                p[0][ref[i][1]] = cur
                p[1][ref[i][1]] = cur
                i+=1
        else:
            pos = False
            break
        cur -= 1

    
    if pos:
        print("YES")
        print(*p[0])
        print(*p[1])
    else:
        print("NO")