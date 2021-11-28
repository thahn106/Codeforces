def main():
    test_cases = int(input())
    for t in range(test_cases):
        n,m = input().split()
        n = int(n)
        m = int(m)


        # candidates = [-1 for i in range(n)]
        # # complexity O(nm)
        # for line in range(m):
        #     l,r,x = input().split()
        #     l = int(l)
        #     r = int(r)
        #     x = int(x)
        #     for i in range(l-1,r):
        #         if candidates[i] == -1:
        #             candidates[i] = x
        #         else:
        #             candidates[i]= candidates[i]&x

        # complexity O(mlogm)
        ops = []
        for line in range(m):
            l,r,x = input().split()
            l = int(l)
            r = int(r)
            x = int(x)
            start = (l-1, False, x)
            end = (r-1, True, x)
            ops.append(start)
            ops.append(end)
        ops.sort()

        counter = 0
        walk, op, val= ops[counter]
        candidates = [-1 for i in range(n)]
        tim = []
        #complexity O(2m)
        for i in range(n):
            while(walk==i):
                if (op):
                    tim.remove(val)
                    value = 0
                    for ti in tim:
                        if value == 0:
                            value=ti
                        else:
                            value = value & ti
                else:
                    tim.append(val)
                    value = value & val
                counter +=1
                if counter < 2*m:
                    walk, op, val = ops[counter]
                else:
                    walk = n
            candidates[i]= value

        # complexity O(n)
        total = -1
        for cand in candidates:
            if total == -1:
                total = cand
            else:
                total = total | cand
        # complexity O(n)
        for exp in range(n-1):
            total = total*2
            if total > 1000000007:
                total -= 1000000007
        print(total)

if __name__ == "__main__":
    main()
