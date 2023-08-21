import sys

input = sys.stdin.readline




for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    max_val = 0
    min_val = 0
    max_ind = 0
    min_ind = 0
    pos_count = 0
    neg_count = 0


    
    for i in range(n):
        if a[i] > 0:
            pos_count += 1
        elif a[i] < 0:
            neg_count += 1
        if a[i]>max_val:
            max_val = a[i]
            max_ind = i
        if a[i]<min_val:
            min_val = a[i]
            min_ind = i

    ans = []
    def action(x,y):
        ans.append([x+1,y+1])
        a[x] += a[y]

    def in_bound(x):
        return 0 <= x < n


    # setup NAIVE
    if max_val > - min_val:
        if neg_count <= 11:
            dir = 1
            action(0, max_ind)
            if a[0] < max_val:
                action(0, max_ind)
            cur = 0
        elif neg_count == 12:
            if a[n-1] >=0:
                if a[n-2] < 0 :
                    while a[n-2]>-20:
                        action(n-2,n-2)
                        cur = n-2
                        dir = -1
                elif a[n-2] == 0:
                    while a[min_ind] > -20:
                        action(min_ind, min_ind)
                    action(n-3, min_ind)
                    while a[n-3] > -20:
                        action(n-3, min_ind)
                    cur = n-3
                    dir = -1
                else:
                    while a[min_ind] > -20:
                        action(min_ind, min_ind)
                    while a[n-2] > -20:
                        action(n-2, min_ind)
                    cur = n-2
                    dir = -1
            else:
                if min_val == -1:
                    action(n-1, min_ind)
                    while a[n-1]>-20:
                        action(n-1,n-1)
                        cur = n-1
                        dir = -1
                else:
                    cur = n-1
                    dir = -1
                    while a[cur] == -1:
                        cur -= 1
                    cur += 1
                    if cur < n-1:
                        while a[cur] > -20:
                            action(cur, cur)
                        cur = n-2
                    else:
                        action(n-1, max_ind)
                        action(n-1, max_ind)
                        cur = n-2
                        while a[cur] >= 0:
                            cur -= 1
                        st = cur
                        cur += 1
                        dir = 1
                        while in_bound(cur+dir):
                            while dir*(a[cur+dir] - a[cur]) < 0:
                                action(cur+dir, cur)
                            cur += dir
                        cur = st
                        dir = -1
        else:
            if a[n-1] <0:
                while a[n-1]>-20:
                    action(n-1,n-1)
                    cur = n-1
                    dir = -1
            else:
                while a[min_ind] > -20:
                    action(min_ind, min_ind)
                while a[n-2] > -20:
                    action(n-2, min_ind)
                cur = n-2
                dir = -1
    elif - min_val > max_val:
        if pos_count <= 11:
            dir = -1
            action(n-1, min_ind)
            if a[n-1] > min_val:
                action(n-1, min_ind)
            cur = n-1
        elif pos_count == 12:
            if a[0] <= 0:
                if a[1] > 0:
                    while a[1]<20:
                        action(1,1)
                        cur = 1
                        dir = 1
                elif a[1] == 0:
                    while a[max_ind] < 20:
                        action(max_ind, max_ind)
                    action(2, max_ind)
                    while a[2] < 20:
                        action(2, max_ind)
                    cur = 2
                    dir = 1
                else:
                    while a[max_ind] < 20:
                        action(max_ind, max_ind)
                    while a[1] < 20:
                        action(1, max_ind)
                    cur = 1
                    dir = 1
            else:
                if max_val >1:
                    action(0, max_ind)
                    while a[0]<20:
                        action(0,0)
                        cur = 0
                        dir = 1
                else:
                    cur = 0
                    dir = 1
                    while a[cur] == 1:
                        cur += dir
                    cur -= 1
                    if cur > 0:
                        while a[cur] < 20:
                            action(cur, cur)
                        cur = 1
                    else:
                        action(0, min_ind)
                        action(0, min_ind)
                        cur = 1
                        while a[cur] <= 0:
                            cur += 1
                        st = cur
                        cur -= 1
                        dir = -1
                        while in_bound(cur+dir):
                            while dir*(a[cur+dir] - a[cur]) < 0:
                                action(cur+dir, cur)
                            cur += dir
                        cur = st
                        dir = 1

                    

        else:
            if a[0] > 0:
                while a[0]<20:
                    action(0,0)
                    cur = 0
                    dir = 1
            else:
                while a[max_ind] < 20:
                    action(max_ind, max_ind)
                while a[1] < 20:
                    action(1, max_ind)
                cur = 1
                dir = 1
    else: # max_val == -min_val
        if pos_count >= neg_count:
            dir = 1
            action(0, max_ind)
            if a[0] < max_val:
                action(0, max_ind)
            cur = 0
        else:
            dir = -1
            action(n-1, min_ind)
            if a[n-1] > min_val:
                action(n-1, min_ind)
            cur = n-1


    

    while in_bound(cur+dir):
        while dir*(a[cur+dir] - a[cur]) < 0:
            action(cur+dir, cur)
        cur += dir

    print(len(ans))
    for x in ans:
        print(*x)
